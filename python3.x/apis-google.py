https://console.cloud.google.com/google/maps-apis/new?project=upbeat-lexicon-223120

Geocoding maps-apis
Distance Matrix maps-apis
pip install geolocation-python

# -- coding: utf-8 --

from geolocation.main import GoogleMaps from geolocation.distance_matrix.client import DistanceMatrixApiClient

address = “New York City Wall Street 12”

google_maps = GoogleMaps(api_key=’your_google_maps_key’)

location = google_maps.search(location=address) # sends search to Google Maps.

print(location.all()) # returns all locations.

my_location = location.first() # returns only first location.

print(my_location.city) print(my_location.route) print(my_location.street_number) print(my_location.postal_code)

for administrative_area in my_location.administrative_area:
print(“{}: {} ({})”.format(administrative_area.area_type,
administrative_area.name, administrative_area.short_name))
print(my_location.country) print(my_location.country_shortcut)

print(my_location.formatted_address)

print(my_location.lat) print(my_location.lng)

# reverse geocode

lat = 40.7060008 lng = -74.0088189

my_location = google_maps.search(lat=lat, lng=lng).first()



# -- coding: utf-8 --

from geolocation.main import GoogleMaps from geolocation.distance_matrix.client import DistanceMatrixApiClient

origins = [‘rybnik’, ‘oslo’] destinations = [‘zagrzeb’]

google_maps = GoogleMaps(api_key=’your_google_maps_key’)

items = google_maps.distance(origins, destinations).all() # default mode parameter is DistanceMatrixApiClient.MODE_DRIVING.

for item in items:
print(‘origin: %s’ % item.origin)

print(‘destination: %s’ % item.destination)

print(‘km: %s’ % item.distance.kilometers)

print(‘m: %s’ % item.distance.meters)

print(‘miles: %s’ % item.distance.miles)

print(‘duration: %s’ % item.duration) # returns string.

print(‘duration datetime: %s’ % item.duration.datetime) # returns datetime.

# you can also get items from duration, returns int() values. print(‘duration days: %s’ % item.duration.days)

print(‘duration hours: %s’ % item.duration.hours)

print(‘duration minutes: %s’ % item.duration.minutes)

print(‘duration seconds: %s’ % item.duration.seconds)



# Bicicleta
items = google_maps.distance(origins, destinations, DistanceMatrixApiClient.MODE_BICYCLING).all()

for item in items:
print(‘origin: %s’ % item.origin)

print(‘destination: %s’ % item.destination)

print(‘km: %s’ % item.distance.kilometers)

print(‘m: %s’ % item.distance.meters)

print(‘miles: %s’ % item.distance.miles)

print(‘duration: %s’ % item.duration)
