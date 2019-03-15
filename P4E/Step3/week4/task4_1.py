#!/usr/bin/env python

#About getting url from web

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_156951.html'
html = urllib.request.urlopen(url, context = ctx).read()
numbs = BeautifulSoup(html, "html.parser")

spans = numbs("span")

counter = 0
for span in spans:
    counter += int(span.contents[0])

print(counter)