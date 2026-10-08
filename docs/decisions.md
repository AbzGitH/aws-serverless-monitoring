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

## Lambda IAM Trust Policy

`iam/trust-policy.json` allows the AWS Lambda service (`lambda.amazonaws.com`) to assume the Development execution role.

Trust policy = who can use the role.  
Permissions policy = what the role can do.

## Lambda DynamoDB Access

The Development Lambda function uses the execution role:

`serverless-monitoring-dev-role`

A project-specific inline IAM policy grants access only to:

`serverless-monitoring-dev`

Allowed actions:

- `dynamodb:PutItem` — write an item to the table.
- `dynamodb:GetItem` — retrieve an item from the table.

Resource scope:

`arn:aws:dynamodb:eu-west-2:560396669076:table/serverless-monitoring-dev`

### Least-Privilege Concept

The Lambda function is granted only the actions and resource access required by the application rather than broad permissions such as `dynamodb:*`.

### Implementation Process

1. Create the DynamoDB table.
2. Retrieve the table ARN.
3. Define the required DynamoDB actions in `iam/dynamodb-policy.json`.
4. Restrict the policy to the exact table ARN.
5. Attach the policy to the Lambda execution role.
6. Verify the attached policy with `aws iam get-role-policy`.

### Key Concepts

- ARN = the unique AWS address of a resource.
- Trust policy = who can assume a role.
- Permissions policy = what the role can do.
- Least privilege = only the required actions against the required resources.
