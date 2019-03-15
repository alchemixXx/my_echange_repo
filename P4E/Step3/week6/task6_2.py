#!/usr/bin/env python

import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

static = "http://py4e-data.dr-chuck.net/json?"

address = "Technical University of Cluj-Napoca"

url = static + urllib.parse.urlencode({"key":api_key}) + "&" + urllib.parse.urlencode({'address': address})



data = urllib.request.urlopen(url).read()
result = json.loads(data)
x = json.dumps(result, indent=4)


# print(data)
# print(x)

print(result["results"][0]["place_id"])