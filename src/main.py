#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import sys
import os
import json
import datetime
import config
import dynamo

# Import vendor modules from a separate directory
here = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(here, "./vendored"))

import healthcheck
import tweet

SERVICE_DOWN = "Nysseituu, voihan pahus! :("
SERVICE_UP = "Nysset kulkee, ainakin kartalla. :)"


def handler(event, context):
    checks = [healthcheck.check_site(site) for site in config.sites_to_check]
    all_ok = all([check["health"] == "UP" for check in checks])
    message = SERVICE_UP if all_ok else SERVICE_DOWN

    result = {
        "message": message,
        "service_is_up": all_ok,
        "healthchecks": checks,
        "timestamp": datetime.datetime.utcnow().isoformat() + 'Z'
    }
    print(json.dumps(result, indent=1))

    last_state_change = dynamo.get("last_state_change")
    if last_state_change:
        if last_state_change["service_is_up"] is not all_ok:
            print("State has changed from {} to {}".format(last_state_change["service_is_up"], all_ok))
            if tweet.is_tweeting_allowed():
                api = tweet.get_twitter_api()
                status = api.PostUpdate(message)
                print(status)
        else:
            print("No change in state: {}".format(all_ok))
    else:
        print("No previous state data found")
        last_state_change = {
            "service_is_up": result["service_is_up"],
            "last_changed": result["timestamp"]
        }
        dynamo.put("last_state_change", last_state_change)

    dynamo.put("latest_healthcheck", result)
    return all_ok


if __name__ == "__main__":
    print("Local execution is not supported. Please run this in AWS Lambda.")
