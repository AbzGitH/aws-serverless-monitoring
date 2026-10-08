import json
import uuid
import boto3

# Create a DynamoDB resource in the same AWS region as the Lambda function.
dynamodb = boto3.resource("dynamodb")

# Development table used by this Lambda function.
table = dynamodb.Table("serverless-monitoring-dev")


def lambda_handler(event, context):
    # Generate a unique ID for each incoming request.
    request_id = str(uuid.uuid4())

    # Store a simple application record in DynamoDB.
    table.put_item(
        Item={
            "requestId": request_id,
            "message": "Serverless monitoring request received"
        }
    )

    # Return a successful HTTP-style response.
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Request stored successfully",
            "requestId": request_id
        })
    }