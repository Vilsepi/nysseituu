#!/usr/bin/env python
# -*- coding: utf-8 -*-

import config
import healthcheck
import tweet

status = [healthcheck.check_site(site) for site in config.sites_to_check]
print status

api = tweet.get_twitter_api(False)
tweeting_allowed = tweet.is_tweeting_allowed()

if tweeting_allowed:
    message = 'Kulkeekohan pukki nyssellä?'
    status = api.PostUpdate(message)
    print status
