#!/usr/bin/env python
# -*- coding: utf-8 -*-

import helpers
import twitter

api = twitter.Api(consumer_key=helpers.getConsumerKeyEnv(),
                  consumer_secret=helpers.getConsumerSecretEnv(),
                  access_token_key=helpers.getTokenKeyEnv(),
                  access_token_secret=helpers.getTokenSecretEnv(),
                  input_encoding='utf-8')

print api.VerifyCredentials()

tweeting_allowed = helpers.getTweetingAllowedEnv()

if tweeting_allowed:
    message = 'Nysse on korjattu!'
    status = api.PostUpdate(message)
    print status
