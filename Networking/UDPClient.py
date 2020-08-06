#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 11:25:02 2020

@author: lex
"""

import socket
host="127.0.0.1"
port=7777
try:
    message=input("What Message you want to send?")
    client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    client.bind((host,port))
    client.sendto(message.encode(), (host,port))
    data =client.recv(4096)
    print(data.decode())
finally:
    client.close()
    print("Finished execution services closed")