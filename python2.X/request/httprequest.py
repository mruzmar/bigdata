import requests
r = requests.get("http://www.elpais.com")

print (r.status_code)
print (r.headers)
print (r.content)


r = requests.get("https://api-cdn.parkimeter.com/parkings?type=booking&arrival=2018-03-13T20%3A00%3A00.000Z&departure=2018-03-14T18%3A00%3A00.000Z&latitude=40.403874&longitude=-3.706646")
print (r.status_code)
print (r.headers)
print (r.content)
