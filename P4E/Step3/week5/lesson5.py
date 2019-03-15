#!/usr/bin/env python

import xml.etree.ElementTree as ET

data = '''<person>
 <name> Chuck</name>
 <phone type="init">+1 734 303 4456
 </phone>
 <email hide="yes"/>
 </person>'''

tree = ET.fromstring(data)
print(tree)
print("Name:", tree.find('name').text)
print("Attr", tree.find('email').get('hide'))
print("Phone", tree.find('phone').text)