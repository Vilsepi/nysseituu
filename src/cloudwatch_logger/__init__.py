# -*- coding: utf-8 -*-

import time
import boto3


# This does not cache the stream token so that several concurrent lambdas could log into
# the same stream. However, this is not scalable and probably not that safe either.
class CloudWatchLogger:

    def __init__(self):
        self.client = boto3.client("logs")

    def log(self, message):
        streams = self.client.describe_log_streams(
            logGroupName="nysseituu-dev",
            logStreamNamePrefix="state-changes"
        )
        params = {
            "logGroupName": "nysseituu-dev",
            "logStreamName": "state-changes",
            "logEvents": [
                {
                    "timestamp": int(round(time.time() * 1000)),
                    "message": message
                },
            ]
        }
        token = streams.get("logStreams")[0].get("uploadSequenceToken", None)
        if token:
            params["sequenceToken"] = token
        self.client.put_log_events(**params)
