import boto3
import os
import json


def sendRes(status, body):
    return {
        'statusCode': status,
        'headers': {
            'Content-Type': 'text/html'
        },
        'body': body
    }


def handler(event, context):
    print('request: {}'.format(json.dumps(event)))

    dynamodb = boto3.client('dynamodb')

    dynamodb.update_item(
        TableName=os.environ['HITS_TABLE_NAME'],
        Key={
            'path': {
                'S': event.rawPath
            }
        },
        UpdateExpression='ADD hits :incr',
        ExpressionAttributeValues={
            ':incr': {
                'N': '1'
            }
        }
    )
    print('inserted counter for ' + event.rawPath)
    return sendRes(200, 'You have connected with the Lambda!')
