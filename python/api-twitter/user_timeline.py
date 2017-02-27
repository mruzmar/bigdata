#!/usr/bin/python

#-----------------------------------------------------------------------
# twitter-user-timeline
#  - displays el timeline de usuario.
#  Más info https://github.com/ideoforms/python-twitter-examples/blob/master/twitter-user-timeline.py
#-----------------------------------------------------------------------

from twitter import *

#-----------------------------------------------------------------------
# load our API credentials
#-----------------------------------------------------------------------
config = {}
execfile("config.py", config)


twitter = Twitter(
		auth = OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))


user = "mruz"


results = twitter.statuses.user_timeline(screen_name = user)


for status in results:
	print "(%s) %s" % (status["created_at"], status["text"].encode("ascii", "ignore"))
