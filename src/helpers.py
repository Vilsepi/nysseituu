#!/usr/bin/env python

import os

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
