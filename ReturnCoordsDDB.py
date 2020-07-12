import json
import boto3
client = boto3.client('dynamodb')
def lambda_handler(event, context):
    y = []
    response = client.batch_get_item( RequestItems={'generic': {
            'Keys': [
                { 'pk': { 'S': 'coords'}, 'sk': { 'S': '1' } },
                { 'pk': { 'S': 'coords'}, 'sk': { 'S': '2' } },
                { 'pk': { 'S': 'coords'}, 'sk': { 'S': '3' } },
                { 'pk': { 'S': 'coords'}, 'sk': { 'S': '4' } },
                { 'pk': { 'S': 'coords'}, 'sk': { 'S': '5' } }
            ],
            'AttributesToGet': ['latitude','longitude']}})
    for item in response['Responses']['generic']:
        y.append({ "type": "point", "longitude": item['longitude']['N'], "latitude": item['latitude']['N'] })
    return { 'statusCode': 200,  'body': json.dumps(y), 'headers': {'Content-Type': 'application/json','Access-Control-Allow-Origin': '*','Access-Control-Allow-Methods':'*'}}
