#pip install pygeocoder
from pygeocoder import Geocoder
results = Geocoder.geocode("Gran vía 22, 2D 28006 Madrid")
print(results[0].coordinates)
print(results[0])
