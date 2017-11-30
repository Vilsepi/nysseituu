
import boto3
import os


class DBClient:

    def __init__(self):
        self.table_name = os.environ.get("NYSSEITUU_TABLE_NAME", None)
        self.table = None
        self.dynamo_available = os.environ.get("IN_AWS", "false").lower() == "true"
        if self.dynamo_available:
            self.table = boto3.resource("dynamodb").Table(self.table_name)

    def put(self, key, item):
        item["key"] = key
        if self.dynamo_available:
            response = self.table.put_item(Item=item)
            return response
        else:
            print("Local support for dynamodb not implemented")
            return {}

    def get(self, key):
        if self.dynamo_available:
            response = self.table.get_item(TableName=self.table_name, Key={"key": key})
            return response.get("Item")
        else:
            return None
