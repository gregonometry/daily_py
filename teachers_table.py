import boto3
import json



def lambda_handler(event, context):
    print(json.dumps(event))
    try:
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.table('teachers')
        table.put_item(
            Item={'Grade': 1, 'Subject': 'Math', 'LastName': 'Ferguson'})
        table.put_item(
            Item={'Grade': 1, 'Subject': 'English', 'LastName': 'Bilby'})
        table.put_item(
            Item={'Grade': 1, 'Subject': 'Gym', 'LastName': 'Stuart'})
        table.put_item(
            Item={'Grade': 4, 'Subject': 'English', 'LastName': 'Isaac'})
    except Exception:
        print(event)
