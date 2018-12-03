import urllib.request as url
import json

request      = "http://ip-api.com/json"
response     = url.urlopen( request )
str_response = response.readall().decode('utf-8')
obj          = json.loads(str_response)

print("Actualmente estas en: %s" % obj['country'])