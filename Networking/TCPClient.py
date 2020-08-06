#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 11:25:02 2020

@author: lex
"""

import socket
host="www.google.com"
port=80
request="GET / HTTP/1.1\r\nHost:www.google.com\r\n\r\n"
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((host,port))
client.send(request.encode())
response=client.recv(4098)
print(response.decode())
client.close()