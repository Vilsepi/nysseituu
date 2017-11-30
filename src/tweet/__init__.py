# -*- coding: utf-8 -*-

import os
import twitter


def is_tweeting_allowed():
    if os.environ.get("TWEETING_ALLOWED", None) == "True":
        return True
    else:
        return False


def get_twitter_api(verify=False):
    api = twitter.Api(consumer_key=os.environ.get("TWITTER_CONSUMER_KEY", None),
                      consumer_secret=os.environ.get("TWITTER_CONSUMER_SECRET", None),
                      access_token_key=os.environ.get("TWITTER_TOKEN_KEY", None),
                      access_token_secret=os.environ.get("TWITTER_TOKEN_SECRET", None),
                      input_encoding='utf-8')
    if verify:
        response = api.VerifyCredentials()
        print(response)
    return api
