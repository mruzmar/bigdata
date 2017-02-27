#!/usr/bin/python

#-----------------------------------------------------------------------
# twitter-friends
#  - lista los followers
#-----------------------------------------------------------------------

from twitter import *


config = {}
execfile("config.py", config)


twitter = Twitter(
		auth = OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))


username = "mruz"


query = twitter.friends.ids(screen_name = username)


print "found %d friends" % (len(query["ids"]))

#-----------------------------------------------------------------------
# bucle for en bloques de 100
#-----------------------------------------------------------------------
for n in range(0, len(query["ids"]), 100):
	ids = query["ids"][n:n+100]


	subquery = twitter.users.lookup(user_id = ids)

	for user in subquery:
		print " [%s] %s - %s" % ("*" if user["verified"] else " ", user["screen_name"], user["location"])
