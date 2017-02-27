#!/usr/bin/python
#-----------------------------------------------------------------------
# twitter-search-geo
#  - salida a un fichero CSV.
#-----------------------------------------------------------------------
from twitter import *
import sys
import csv
latitude = 40.438072163753745   # Madrid
longitude = -3.6795366500000455 #
max_range = 1                   # Kilómetros - radio search range in kilometres
num_results = 50                # Mínimo resultados a obtener
outfile = "output.csv"

config = {}
execfile("config.py", config)

twitter = Twitter(
                        auth = OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))
#-----------------------------------------------------------------------
# Se abre fichero para escritura (modo "w")
#-----------------------------------------------------------------------
csvfile = file(outfile, "w")
csvwriter = csv.writer(csvfile)

row = [ "user", "text", "latitude", "longitude" ]
csvwriter.writerow(row)
#-----------------------------------------------------------------------
# El Api de twitter solo permite recoger 100 tweets a la vez
#-----------------------------------------------------------------------
result_count = 0
last_id = None
while result_count <  num_results:

        query = twitter.search.tweets(q = "", geocode = "%f,%f,%dkm" % (latitude, longitude, max_range), count = 100, max_id = last_id)
        for result in query["statuses"]:
                #-----------------------------------------------------------------------
                # Solo procesos con geolocalización
                #-----------------------------------------------------------------------
                if result["geo"]:
                        print str(result)
                        user = result["user"]["screen_name"]
                        text = result["text"]
                        text = text.encode('ascii', 'replace')
                        latitude = result["geo"]["coordinates"][0]
                        longitude = result["geo"]["coordinates"][1]
                        #-----------------------------------------------------------------------
                        # Escribimos al fichero csv
                        #-----------------------------------------------------------------------
                        row = [ user, text, latitude, longitude ]
                        csvwriter.writerow(row)
                        result_count += 1
                last_id = result["id"]

        print "Obtenemos %d resultados" % result_count


csvfile.close()
print "written to %s" % outfile
