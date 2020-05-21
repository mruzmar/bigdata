
from twitter import *
import sys
import csv

#Variables that contains the user credentials to access Twitter API 


access_token = "15002884-QxpvkW1jNTQ3YpO9Vn4yW9Cx8n7UyvwdVzVkrmMbw"
access_token_secret = "eaFWhbH2Mn1trxlYoKlLZsk3nzkk4wsiaFTyIkDbLEYob"
consumer_key = "C1voYrjnzAcwjRU1k8SmL72vK"
consumer_secret = "Uvk3ljIL8duuLM7XxLXrlXBBEkHDl040dxgJox8p9pdJVcxRjh"

# max twitters to get
num_results = 50   

outfile = "output_twitter.csv"
#-----------------------------------------------------------------------
# Se abre fichero para escritura (modo "w")
#-----------------------------------------------------------------------
csvfile = file(outfile, "w")
csvwriter = csv.writer(csvfile)

row = [ "user", "text", "latitude", "longitude" ]

row = "user"+"|"+"text"
csvwriter.writerow(row)

# Busqueda geo en twitter
latitude = 40.438072163753745   # Madrid
longitude = -3.6795366500000455 #
max_range = 10                   # Kilometros - radio search range in kilometres





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


query = twitter.search.tweets(q = "covid", count=1)

#-----------------------------------------------------------------------
# How long did this query take?
#-----------------------------------------------------------------------


#-----------------------------------------------------------------------
# Loop through each of the results, and print its content.
#-----------------------------------------------------------------------


with open('data.json', 'w') as f:
        for result in query["statuses"]:
            #print(query["statuses"])
            json.dump(result, f)




    