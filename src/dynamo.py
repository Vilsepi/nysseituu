
import boto3

table_name = "nysseituu"

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(table_name)


# Create/Update item into DynamoDB. Item must contain key.
def put(item):
    response = table.put_item(Item=item)
    return response

# Create/Update item into DynamoDB. Key is inserted into item.
def put(key, item):
    item["key"] = key
    response = table.put_item(Item=item)
    return response

# Get item by key from DynamoDB.
def get(key):
    response = table.get_item(TableName=table_name, Key={'key': key})
    return response.get("Item")
