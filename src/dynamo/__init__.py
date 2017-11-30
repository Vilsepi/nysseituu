
import boto3
import os


dynamodb = boto3.resource("dynamodb")
table_name = os.environ.get("NYSSEITUU_TABLE_NAME", None)
table = dynamodb.Table(table_name)


def put(key, item):
    item["key"] = key
    response = table.put_item(Item=item)
    return response


def get(key):
    response = table.get_item(TableName=table_name, Key={"key": key})
    return response.get("Item")
