#!/usr/bin/env python3

# Crafted by an AI..

import os
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import yaml

SCHEMAS_DIR = Path(__file__).parent.parent / "schemas"
DOCS_DIR = Path(__file__).parent.parent / "docs"


@dataclass
class SecondaryTable:
    anchor: str
    name: str
    headers: List[str]
    rows: List[List[str]]


def rel_schema_path(schema_path: Path) -> Path:
    """Get schema path relative to the schemas directory."""
    return schema_path.relative_to(SCHEMAS_DIR)


def rel_docs_path(schema_path: Path) -> Path:
    """Get the corresponding docs path for a schema file."""
    return DOCS_DIR / rel_schema_path(schema_path).with_suffix(".md")


def load_yaml(path: Path) -> Dict[str, Any]:
    """Load a YAML file and return its contents as a dict."""
    try:
        with open(path, "r") as f:
            return yaml.safe_load(f)
    except Exception as e:
        print(f"Error loading YAML file {path}: {e}")
        return {}


def ref_to_md_link(ref: Optional[str], schema_ref: Optional[str] = None) -> str:
    """Convert a $ref or $schemaRef to a markdown link."""
    if isinstance(schema_ref, str) and schema_ref.startswith("/"):
        md_path = f"/docs{schema_ref.rsplit('.', 1)[0]}.md"
        link_text = os.path.basename(schema_ref.split("#", 1)[0])
        return f"[{link_text}]({md_path})"
    if isinstance(ref, str) and ref.startswith("/"):
        if "#" in ref:
            path_part, fragment = ref.split("#", 1)
            md_path = f"/docs{path_part.rsplit('.', 1)[0]}.md#{fragment}"
        else:
            md_path = f"/docs{ref.rsplit('.', 1)[0]}.md"
        link_text = os.path.basename(ref.split("#", 1)[0])
        return f"[{link_text}]({md_path})"
    if isinstance(ref, str) and ref.startswith("/"):
        return f"[{ref}]({ref})"
    return str(ref) if ref else ""


def enum_links_from_schema_enum(enum_vals: List[Any]) -> str:
    """Render enum values as markdown links if possible."""
    return ", ".join(
        ref_to_md_link(e, e) if isinstance(e, str) else str(e) for e in enum_vals
    )


def make_anchor(prefix: str, name: str) -> str:
    """Generate a markdown anchor from a prefix and property name."""
    return f"{prefix}-{name}".replace("_", "-").replace(" ", "-")


def singularize(name: str) -> str:
    """Convert a plural property name to singular for table anchors."""
    if name.endswith("ies"):
        return name[:-3] + "y"
    elif name.endswith("s") and not name.endswith("ss"):
        return name[:-1]
    return name


def render_markdown_table(headers: List[str], rows: List[List[str]]) -> List[str]:
    """Render a markdown table from headers and rows."""
    lines = ["| " + " | ".join(headers) + " |"]
    lines.append("|" + "|".join(["---"] * len(headers)) + "|")
    for row in rows:
        lines.append("| " + " | ".join(str(x) for x in row) + " |")
    return lines


def write_readme_index(readme_path: Path, generated_files: List[Path]) -> None:
    """Write the README.md index of all generated markdown files."""
    with open(readme_path, "w") as readme:
        readme.write("# Schema Documentation Index\n\n")
        for md_file in sorted(
            generated_files, key=lambda p: str(p.relative_to(DOCS_DIR))
        ):
            rel_md = md_file.relative_to(DOCS_DIR)
            readme.write(f"- [{rel_md}]({rel_md})\n")


def get_type_column(name: str, prop: dict) -> str:
    """Determine the Type column value for a property."""
    typ = prop.get("type", "")
    ref = prop.get("$ref")
    schema_ref = prop.get("$schemaRef")
    # $schemaRef link
    if schema_ref and not isinstance(schema_ref, dict):
        ref_link = ref_to_md_link(ref, schema_ref)
        return f"$ref: {ref_link}"
    # Special case: no type, has $ref, no $schemaRef, and $ref is /common-1.json#/definitions/...
    if (
        not typ
        and ref
        and not schema_ref
        and ref.startswith("/common-1.json#/definitions/")
    ):
        return ref.split("/")[-1]
    # Array of $schemaRef
    if (
        typ == "array"
        and isinstance(prop.get("items"), dict)
        and "$schemaRef" in prop["items"]
    ):
        items = prop["items"]
        item_schema_ref = items["$schemaRef"]
        link = ref_to_md_link(None, item_schema_ref)
        return f"array of $ref to {link}"
    # Array of embedded objects (secondary table)
    if (
        typ == "array"
        and isinstance(prop.get("items"), dict)
        and "properties" in prop["items"]
    ):
        anchor = make_anchor("array", name)
        return f"array of [{name}](#{anchor})"
    # Object with properties (secondary table)
    if typ == "object" and "properties" in prop:
        anchor = make_anchor("object", name)
        return f"[{name}](#{anchor})"
    return typ


def get_possible_values_column(prop: dict) -> str:
    """Determine the Possible Values column for a property."""
    schema_ref = prop.get("$schemaRef")
    # Enum for $schemaRef as object
    if (
        isinstance(schema_ref, dict)
        and schema_ref.get("type") == "object"
        and "properties" in schema_ref
        and "$schema" in schema_ref["properties"]
        and "enum" in schema_ref["properties"]["$schema"]
    ):
        enum_vals = schema_ref["properties"]["$schema"]["enum"]
        return enum_links_from_schema_enum(enum_vals)
    elif "enum" in prop and prop["enum"]:
        return ", ".join(map(str, prop["enum"]))
    return ""


def get_description_column(prop: dict) -> str:
    """Return the Description column for a property, handling multi-line text for markdown tables without trailing <br>."""
    desc = prop.get("description", "")
    if desc:
        desc = str(desc).strip()
        desc = desc.replace("\n", "<br>")
    return desc


def handle_secondary_tables(
    name: str,
    prop: dict,
    secondary_tables: List[SecondaryTable],
) -> None:
    """If the property is an array/object with embedded properties, add a secondary table."""
    typ = prop.get("type", "")
    # Array of embedded objects
    if (
        typ == "array"
        and isinstance(prop.get("items"), dict)
        and "properties" in prop["items"]
    ):
        items = prop["items"]
        anchor = make_anchor("array", name)
        singular = singularize(name)
        item_headers, item_rows = build_markdown_table_from_properties(
            items["properties"], items.get("required", []), secondary_tables
        )
        secondary_tables.append(
            SecondaryTable(anchor, singular, item_headers, item_rows)
        )
    # Object with properties
    elif typ == "object" and "properties" in prop:
        anchor = make_anchor("object", name)
        obj_headers, obj_rows = build_markdown_table_from_properties(
            prop["properties"], prop.get("required", []), secondary_tables
        )
        secondary_tables.append(SecondaryTable(anchor, name, obj_headers, obj_rows))


def build_property_row(
    name: str,
    prop: dict,
    required_fields: set,
    secondary_tables: List[SecondaryTable],
) -> List[str]:
    """Build a markdown table row for a single property."""
    # Add secondary tables if needed
    handle_secondary_tables(name, prop, secondary_tables)
    return [
        name,
        get_type_column(name, prop),
        "yes" if name in required_fields else "no",
        get_possible_values_column(prop),
        get_description_column(prop),
    ]


def build_markdown_table_from_properties(
    properties: Dict[str, Any],
    required_fields: List[str],
    secondary_tables: List[SecondaryTable],
) -> Tuple[List[str], List[List[str]]]:
    """Build the main and secondary markdown tables for schema properties."""
    headers = ["Name", "Type", "Required", "Possible Values", "Description"]
    required_fields_set = set(required_fields or [])
    rows = [
        build_property_row(name, prop, required_fields_set, secondary_tables)
        for name, prop in properties.items()
    ]
    return headers, rows


def generate_markdown(schema_path: Path, schema: Dict[str, Any]) -> str:
    """Generate the full markdown documentation for a schema file."""
    rel_path = rel_schema_path(schema_path)
    rel_path_str = "/" + str(rel_path)
    schema_file_link = f"/schemas/{rel_path}"
    title = schema.get("title") or rel_path_str
    description = schema.get("description") or "No description"
    md: List[str] = [
        f"# {title}",
        "",
        f"**Schema location:** [{rel_path_str}]({schema_file_link})",
        "",
        f"**Description:** {description}",
        "",
    ]
    properties = schema.get("properties", {})
    required_fields = schema.get("required", [])
    secondary_tables: List[SecondaryTable] = []
    headers, rows = build_markdown_table_from_properties(
        properties, required_fields, secondary_tables
    )
    if rows:
        md.extend(render_markdown_table(headers, rows))
    else:
        md.append("_No properties defined._")
    # Write secondary tables
    for table in secondary_tables:
        md.append(f'\n### <a name="{table.anchor}"></a>{table.name}')
        md.extend(render_markdown_table(table.headers, table.rows))
    return "\n".join(md)


def main() -> None:
    """Main entry point: generate markdown docs for all schemas."""
    generated_files = []
    for root, _, files in os.walk(SCHEMAS_DIR):
        for file in files:
            if file.endswith(".yml") or file.endswith(".yaml"):
                schema_path = Path(root) / file
                schema = load_yaml(schema_path)
                if not schema:
                    continue
                md = generate_markdown(schema_path, schema)
                out_path = rel_docs_path(schema_path)
                os.makedirs(out_path.parent, exist_ok=True)
                try:
                    with open(out_path, "w") as f:
                        f.write(md)
                    print(f"Generated {out_path}")
                    generated_files.append(out_path)
                except Exception as e:
                    print(f"Error writing {out_path}: {e}")

    # Generate README.md index
    readme_path = DOCS_DIR / "README.md"
    write_readme_index(readme_path, generated_files)
    print(f"Generated {readme_path}")


if __name__ == "__main__":
    main()
