#!/usr/bin/env python

# About getting url from web
#
# import urllib.request, urllib.parse, urllib.error
#
# file = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
#
# for line in file:
#     print(line.decode().strip())

# About parsing the web with Beautiful Soup

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = "https://www.crummy.com/software/BeautifulSoup/bs3/documentation.html"
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")
print(soup)

tags = soup('a')
print(tags)
for tag in tags:
    print(tag.get('href', None))
