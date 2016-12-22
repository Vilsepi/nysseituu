#!/usr/bin/env python
# -*- coding: utf-8 -*-

import config
import healthcheck
import tweet

status = [healthcheck.check_site(site) for site in config.sites_to_check]
print status

api = tweet.getTwitterApi(True)
tweeting_allowed = tweet.getTweetingAllowedEnv()

if tweeting_allowed:
    message = 'Kulkeekohan pukki nyssellä?'
    status = api.PostUpdate(message)
    print status
