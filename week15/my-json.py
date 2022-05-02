#!/usr/bin/env python3

import requests
import json
import argparse

parser = argparse.ArgumentParser(description='creating a parser to add arguments')
    
parser.add_argument('-i', '--ipaddress', dest='myIP', type=str, help='Enter an IP address')

myIP = parser.parse_args().myIP

#print(myIP)

url = (f"http://ipinfo.io/{myIP}/json")

response = requests.get(url)
#print(myIP)
#print(response)

myDict = json.loads(response.text)

#print(myDict.items())

for key in myDict.keys():
  print(f"{key} : {myDict[key]}")
