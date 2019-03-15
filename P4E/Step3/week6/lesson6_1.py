#!/usr/bin/env python

import json
data = '''{
"name":"Chuck",
"phone":{
"type":"intl",
"number":"+1 734 303 44 56"
},
"email":{
"hide":"yes"
}
}'''

info = json.loads(data)
print(type(info))
print(info)
print("Name:", info["name"])
print("Hide: ", info["email"]["hide"])