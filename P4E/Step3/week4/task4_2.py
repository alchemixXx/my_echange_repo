#!/usr/bin/env python

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

names = list()

#create variable to provide a loop
donereps = 0

#Parameters for testing
# repeats = 7
# position = 18

# user-input:
repeats = int(input('Enter number of repeats: '))
position = int(input('Enter required position: '))

while donereps <= repeats:
    if donereps == 0:
        url = input("Ener link: ")
    else:
        url = extracted_links[position - 1]

    html = urllib.request.urlopen(url, context = ctx).read()
    page = BeautifulSoup(html, "html.parser")

    # create list for links
    extracted_links = list()

    links = page("a")

    #add all links to list
    for link in links:
        extracted_links.append(link.get('href', None))


    #add current name to list of names
    x = re.findall("by_(\w+)\.ht..", url)
    names.append(x[0])

    donereps += 1
else:
    print(names[repeats])

