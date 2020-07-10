#!/usr/bin/env python3
'''
24.48.0.1   http://jjip-api.com/json/24.48.0.1
'''

import json
import requests
import socket


def main():

   # hostloc = socket.hostIP()
   # hostIP = socket.gethostbyname(hostloc)
   # userip = socket.gethostbyname(hostIP)
   # print(userLoc)

    # get hostname and IP
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)

    # display hostname and IP
    print(f"Hostname: {hostname}")
    print(f"IP Address: {ip_address}")

    # use requests to send an HTTP GET to ip-api.com/json/IPGOESHERE
    userLoc = requests.get(f"http://ip-api.com/json/{ip_address}")

    # by default, a resusts OBJECT displays teh response code when it is printed
    print(userLoc)

    # this will display JUST the JSON attached off the userLoc
    print(userLoc.json())

main()
