# -*- coding: utf-8 -*-

import requests


def _result(site, health, response=None, message=None):
    result = {
        "name": site["name"],
        "health": health
    }
    if message:
        result["message"] = message
    if response is not None:
        result["status"] = response.status_code
        result["response_time_ms"] = int(response.elapsed.total_seconds() * 1000)
    return result


def check_site(site):
    response = None
    try:
        response = requests.get(site["url"])
        if response.status_code not in site["acceptable_statuses"]:
            print("Bad status code: {}".format(response.status_code))
            return _result(site, "DOWN", response, "Unacceptable status code")
        for mandatory_string in site.get("mandatory_strings", []):
            if mandatory_string not in response.text:
                print("String not found in response: " + mandatory_string)
                return _result(site, "DOWN", response, "String not found in response: {}".format(mandatory_string))
        return _result(site, "UP", response)
    except Exception as err:
        print(err)
        return _result(site, "UNKNOWN", response, "Exception while trying to check site health: {}".format(err))
