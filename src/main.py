#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import config
import healthcheck
import tweet
import boto3


SERVICE_DOWN = "Nysseituu, voihan pahus! :("
SERVICE_UP = "Nysset kulkee, ainakin kartalla. :)"

dynamodb = boto3.resource('dynamodb')

def handler(event, context):
    checks = [healthcheck.check_site(site) for site in config.sites_to_check]
    all_ok = all([check["health"] == "UP" for check in checks])
    result = {"service_is_up": all_ok, "healthchecks": checks}

    message = SERVICE_UP if all_ok else SERVICE_DOWN
    print result, message

    if tweet.is_tweeting_allowed():
        api = tweet.get_twitter_api()
        status = api.PostUpdate(message)
        print status

    table = dynamodb.Table(os.environ.get("TABLE_NAME"))

if __name__ == "__main__":
    handler({},{})
