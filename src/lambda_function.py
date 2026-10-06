import json


def lambda_handler(event, context):
    # Return a successful HTTP-style response.
    return {
        # 200 is the standard HTTP status code for "OK / success".
        "statusCode": 200,

        # API Gateway expects the response body as a string,
        # so json.dumps() converts this Python dictionary into JSON text.
        "body": json.dumps({
            "message": "Serverless monitoring function is working"
        })
    }