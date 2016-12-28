#!/usr/bin/env python
# -*- coding: utf-8 -*-

import config
import healthcheck
import tweet

SERVICE_DOWN = "Nysseituu, voihan pahus! :("
SERVICE_UP = "Nysset kulkee, ainakin kartalla. :)"


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


if __name__ == "__main__":
    handler({},{})
