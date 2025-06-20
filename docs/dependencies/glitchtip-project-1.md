# /dependencies/glitchtip-project-1.yml

**Schema location:** [/dependencies/glitchtip-project-1.yml](/schemas/dependencies/glitchtip-project-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | no | /dependencies/glitchtip-project-1.yml |  |
| labels | labels | no |  |  |
| name | identifierLowercase64 | yes |  |  |
| projectId | identifierLowercase64 | no |  |  |
| description | string | yes |  |  |
| app | $ref: [app-1.yml](/docs/app-sre/app-1.md) | yes |  |  |
| platform | string | yes | cocoa, cocoa-objc, cocoa-swift, cordova, csharp, electron, elixir, go, go-http, java, java-android, java-appengine, java-log4j, java-log4j2, java-logback, java-logging, javascript, javascript-angular, javascript-angularjs, javascript-backbone, javascript-ember, javascript-nextjs, javascript-react, javascript-vue, minidump, native, node, node-connect, node-express, node-koa, other, php, php-laravel, php-monolog, php-symfony, python, python-bottle, python-celery, python-django, python-flask, python-pylons, python-pyramid, python-pythonawslambda, python-rq, python-sanic, python-tornado, react-native, ruby, ruby-rack, ruby-rails, rust |  |
| teams | array of $ref to [glitchtip-team-1.yml](/docs/dependencies/glitchtip-team-1.md) | yes |  |  |
| organization | $ref: [glitchtip-organization-1.yml](/docs/dependencies/glitchtip-organization-1.md) | yes |  |  |
| alerts | array | no |  |  |
| eventThrottleRate | percentage | no |  | Percentage of new events to deny. 0-100 |
| jira | [jira](#object-jira) | no |  |  |

### <a name="object-jira"></a>jira
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| escalationPolicy | $ref: [escalation-policy-1.yml](/docs/app-sre/escalation-policy-1.md) | no |  |  |
| project | string | no |  |  |
| components | array | no |  |  |
| labels | array | no |  |  |