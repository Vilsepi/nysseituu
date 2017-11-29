
import boto3

table_name = "nysseituu"

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(table_name)


def put(key, item):
    item["key"] = key
    response = table.put_item(Item=item)
    return response


def get(key):
    response = table.get_item(TableName=table_name, Key={'key': key})
    return response.get("Item")
