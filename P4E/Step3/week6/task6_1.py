#!/usr/bin/env python

import urllib.request, urllib.parse, urllib.error
import json

url = "http://py4e-data.dr-chuck.net/comments_156954.json"

html = urllib.request.urlopen(url).read()
data = json.loads(html)
# x = json.dumps(data, indent=4)
# print(x)

summ = 0
i = 0
while i < (len(data["comments"])):
    summ += int(data["comments"][i]["count"])
    i += 1

print(summ)