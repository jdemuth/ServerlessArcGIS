import json
import boto3
ddbclient = boto3.client('dynamodb')
def lambda_handler(event, context):
    ddbclient.put_item(Item={'pk': {  'S': 'coords' }, 'sk': {  'S': '1' },'latitude': {  'N': '30.1219005584716' },'longitude': {  'N': '31.4055995941162' } }, TableName='generic')
	ddbclient.put_item(Item={'pk': {  'S': 'coords' }, 'sk': {  'S': '2' },'latitude': {  'N': '35.2140007019042' },'longitude': {  'N': '-80.9430999755859' } }, TableName='generic')
	ddbclient.put_item(Item={'pk': {  'S': 'coords' }, 'sk': {  'S': '3' },'latitude': {  'N': '33.3675003051757' },'longitude': {  'N': '-7.58997011184692' } }, TableName='generic')
	ddbclient.put_item(Item={'pk': {  'S': 'coords' }, 'sk': {  'S': '4' },'latitude': {  'N': '38.805801' },'longitude': {  'N': '-104.700996' } }, TableName='generic')
	ddbclient.put_item(Item={'pk': {  'S': 'coords' }, 'sk': {  'S': '5' },'latitude': {  'N': '55.617900848389' },'longitude': {  'N': '12.656000137329' } }, TableName='generic')