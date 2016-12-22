# -*- coding: utf-8 -*-

import os
import twitter


def _getStringEnv(env_name):
    return os.environ.get(env_name, None)

def isTweetingAllowed():
    if os.environ.get("TWEETING_ALLOWED", None) == "True":
        return True
    else:
        return False

def getTwitterApi(verify=False):
    api = twitter.Api(consumer_key=_getStringEnv("TWITTER_CONSUMER_KEY"),
                      consumer_secret=_getStringEnv("TWITTER_CONSUMER_SECRET"),
                      access_token_key=_getStringEnv("TWITTER_TOKEN_KEY"),
                      access_token_secret=_getStringEnv("TWITTER_TOKEN_SECRET"),
                      input_encoding='utf-8')
    if verify:
        response = api.VerifyCredentials()
        print response
    return api
