

#Variables that contains the user credentials to access Twitter API 


access_token = "15002884-QxpvkW1jNTQ3YpO9Vn4yW9Cx8n7UyvwdVzVkrmMbw"
access_token_secret = "eaFWhbH2Mn1trxlYoKlLZsk3nzkk4wsiaFTyIkDbLEYob"
consumer_key = "C1voYrjnzAcwjRU1k8SmL72vK"
consumer_secret = "Uvk3ljIL8duuLM7XxLXrlXBBEkHDl040dxgJox8p9pdJVcxRjh"

# max twitters to get
num_results = 50   


# Busqueda geo en twitter
latitude = 40.438072163753745   # Madrid
longitude = -3.6795366500000455 #
max_range = 1                   # Kilometros - radio search range in kilometres



from twitter import *

twitter = Twitter(
    auth=OAuth(access_token, access_token_secret, consumer_key, consumer_secret))

# Api search
# https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets

# Get query from twitter geo
#query = twitter.search.tweets(q = "", geocode = "%f,%f,%dkm" % (latitude, longitude, max_range), count = 100, max_id = last_id)

#-----------------------------------------------------------------------
# El Api de twitter solo permite recoger 100 tweets a la vez
#-----------------------------------------------------------------------
import json
result_count = 0
last_id = None
while result_count <  num_results:

    query = twitter.search.tweets(q = "covid",  lang= es,  count = 100, max_id = last_id)
    for result in query["statuses"]:
        print str(result)