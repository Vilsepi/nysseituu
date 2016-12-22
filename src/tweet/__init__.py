# -*- coding: utf-8 -*-

import os
import twitter


def _get_string_env(env_name):
    return os.environ.get(env_name, None)

def is_tweeting_allowed():
    if os.environ.get("TWEETING_ALLOWED", None) == "True":
        return True
    else:
        return False

def get_twitter_api(verify=False):
    api = twitter.Api(consumer_key=_get_string_env("TWITTER_CONSUMER_KEY"),
                      consumer_secret=_get_string_env("TWITTER_CONSUMER_SECRET"),
                      access_token_key=_get_string_env("TWITTER_TOKEN_KEY"),
                      access_token_secret=_get_string_env("TWITTER_TOKEN_SECRET"),
                      input_encoding='utf-8')
    if verify:
        response = api.VerifyCredentials()
        print response
    return api
