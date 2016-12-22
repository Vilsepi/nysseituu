# -*- coding: utf-8 -*-

import os
import twitter


def getConsumerKeyEnv():
    return os.environ.get("TWITTER_CONSUMER_KEY", None)

def getConsumerSecretEnv():
    return os.environ.get("TWITTER_CONSUMER_SECRET", None)

def getTokenKeyEnv():
    return os.environ.get("TWITTER_TOKEN_KEY", None)

def getTokenSecretEnv():
    return os.environ.get("TWITTER_TOKEN_SECRET", None)

def getTweetingAllowedEnv():
    if os.environ.get("TWEETING_ALLOWED", None) == "True":
        return True
    else:
        return False

def getTwitterApi(verify=False):
    api = twitter.Api(consumer_key=getConsumerKeyEnv(),
                      consumer_secret=getConsumerSecretEnv(),
                      access_token_key=getTokenKeyEnv(),
                      access_token_secret=getTokenSecretEnv(),
                      input_encoding='utf-8')
    if verify:
        resp = api.VerifyCredentials()
        print resp
    return api
