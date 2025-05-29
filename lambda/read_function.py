import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('HighAvailabilityTable')

def lambda_handler(event, context):
    try:
        response = table.scan()
        data = response['Items']
        
        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "GET",
                "Access-Control-Allow-Headers": "*"
            },
            "body": json.dumps(data)
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({"error": str(e)})
        }
