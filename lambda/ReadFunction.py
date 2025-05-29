import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('HighAvailabilityTable')

def lambda_handler(event, context):
    try:
        response = table.scan()
        items = response['Items']
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',  # ✅ Required for CORS
                'Access-Control-Allow-Methods': 'GET,OPTIONS',  # Optional but useful
            },
            'body': json.dumps(items)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',  # ✅ Also here
            },
            'body': json.dumps({'error': str(e)})
        }
