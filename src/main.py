#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import sys
import os
import json
import datetime

# Import vendor modules from a separate directory
here = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(here, "./vendored"))

import dynamo
import healthcheck
import tweet
import cloudwatch_logger
import notify

SERVICE_DOWN = "Nysseituu, voihan pahus! :("
SERVICE_UP = "Nysset kulkee, ainakin kartalla. :)"


def get_healthcheck_config(filename):
    with open(filename, "r") as json_file:
        return json.load(json_file)


def handler(event, context):
    config = get_healthcheck_config("healthchecks.json")
    checker = healthcheck.Healthcheck()
    checks = [checker.check_site(site) for site in config]
    service_healthy = all([check["health"] == "UP" for check in checks])
    health = "UP" if service_healthy else "DOWN"
    message = SERVICE_UP if service_healthy else SERVICE_DOWN

    result = {
        "message": message,
        "health": health,
        "healthchecks": checks,
        "timestamp": datetime.datetime.utcnow().isoformat() + 'Z'
    }

    twitter = tweet.TwitterClient()
    db = dynamo.DBClient()
    logger = cloudwatch_logger.CloudWatchLogger()
    notifier = notify.Notifier()

    previous_status_change = db.get("previous_status_change")

    def _update_state():
        current_state = {
            "health": health,
            "timestamp": result["timestamp"]
        }
        db.put("previous_status_change", current_state)

    if previous_status_change:
        if previous_status_change["health"] != health:
            print(f"Service went now {health}!")
            _update_state()
            msg = "Lissu is now {}! It has been {} since {}".format(
                health,
                previous_status_change.get('health').lower(),
                previous_status_change.get('timestamp'))
            logger.log(msg)
            notifier.notify(msg)
            twitter.tweet(message)
        else:
            print(f"Service is still {health} since {previous_status_change.get('timestamp')}")
    else:
        print(f"History not found in cache, service is currently {health}")
        _update_state()

    db.put("latest_healthcheck", result)
    return health


if __name__ == "__main__":
    print("Local execution is not fully supported. Please run this code in AWS Lambda.")
    handler({}, {})
