# -*- coding: utf-8 -*-

import os
import twitter


class TwitterClient:

    def __init__(self, verify_credentials=True):
        self.tweet_live = os.environ.get("TWEETING_ALLOWED", "false").lower() == "true"
        if self.tweet_live:
            self.api = twitter.Api(
                consumer_key=os.environ.get("TWITTER_CONSUMER_KEY", None),
                consumer_secret=os.environ.get("TWITTER_CONSUMER_SECRET", None),
                access_token_key=os.environ.get("TWITTER_TOKEN_KEY", None),
                access_token_secret=os.environ.get("TWITTER_TOKEN_SECRET", None),
                input_encoding='utf-8')
            if verify_credentials:
                response = self.api.VerifyCredentials()
                print(response)
        else:
            self.api = None

    def tweet(self, message):
        if self.tweet_live:
            print(f"Tweeting live: {message}")
            status = self.api.PostUpdate(message)
            print(status)
        else:
            print(f"Not allowed to tweet, but it would have been: {message}")
