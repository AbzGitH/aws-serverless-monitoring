# Architecture

## Overview

This project implements a serverless AWS application using API Gateway, AWS Lambda, Amazon DynamoDB, Amazon CloudWatch and AWS IAM.

![Serverless Monitoring Architecture](serverless-monitoring-architecture.png)

## Request Flow

1. A client sends a request to Amazon API Gateway.
2. API Gateway forwards the request to the AWS Lambda function.
3. Lambda processes the request and writes a record to Amazon DynamoDB.
4. Lambda execution logs and metrics are sent to Amazon CloudWatch.
5. AWS IAM provides the Lambda function with least-privilege permissions.

## Environment Separation

The same Lambda application code is promoted through Development, UAT and Production.

Each environment uses its own DynamoDB table through the `TABLE_NAME` environment variable:

- Development → `serverless-monitoring-dev`
- UAT → `serverless-monitoring-uat`
- Production → `serverless-monitoring-prod`

This keeps application code consistent while separating environment-specific data and permissions.

## Monitoring

Amazon CloudWatch provides:

- Lambda execution logs
- Runtime metrics
- Error monitoring
- A Development Lambda error alarm

This provides operational visibility without requiring dedicated monitoring servers.
