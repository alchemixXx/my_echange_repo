#!/usr/bin/env python

import socket

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

mysocket.connect(("data.pr4e.org", 80))

cmd = "GET http://py4e.com/code3/bs4.zip HTTP/1.0\r\n\r\n".encode()
mysocket.send(cmd)


