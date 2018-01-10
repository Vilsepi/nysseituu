# -*- coding: utf-8 -*-

import os
import boto3


class Notifier:

    def __init__(self):
        self.client = boto3.client('sns')

    def notify(self, message, message_title="Nysseituu health update"):
        self.client.publish(
            TopicArn=os.environ.get("NYSSEITUU_ALARM_TOPIC_ARN", None),
            Message=message,
            Subject=message_title,
            MessageAttributes={
                'AWS.SNS.SMS.SenderID': {
                    'DataType': 'String',
                    'StringValue': 'Nysseituu'
                }
            }
        )
