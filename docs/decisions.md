# Project Decisions

## Naming Convention

Base name:

`serverless-monitoring`

Environment suffixes:

- `-dev`
- `-uat`
- `-prod`

Examples:

- `serverless-monitoring-dev`
- `serverless-monitoring-uat`
- `serverless-monitoring-prod`

Rules:

- Use professional descriptive names.
- Do not include course or project numbering.
- Use lowercase and hyphens where AWS service naming rules allow.
- Add environment suffixes where resources are environment-specific.

## Environment Strategy

Lifecycle:

`Development → UAT → Production`

Implementation:

- Use separate AWS resources per environment for clear isolation.
- Lambda functions:
  - `serverless-monitoring-dev`
  - `serverless-monitoring-uat`
  - `serverless-monitoring-prod`
- DynamoDB tables follow the same environment suffix pattern.
- API Gateway will use a clearly separated environment approach rather than mixing test and production traffic.
- Environment-specific configuration must remain isolated.
- Production changes should only follow successful Development and UAT validation.

Reasoning:

- Prevents test activity from affecting Production.
- Makes environment promotion easy to understand and demonstrate.
- Mirrors common real-world deployment practice without adding unnecessary multi-account complexity.
