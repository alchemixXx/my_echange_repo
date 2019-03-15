#!/usr/bin/env python

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url = input("Enter the URL: ")
url = 'http://py4e-data.dr-chuck.net/comments_156953.xml'
html = urllib.request.urlopen(url, context = ctx)

data = html.read()
tree = ET.fromstring(data)


list_comments = tree.findall("comments")
list_commnet = list_comments[0].findall("comment")

summ = 0

for item in list_commnet:
    number = item.find("count").text
    summ += int(number)

print(summ)


