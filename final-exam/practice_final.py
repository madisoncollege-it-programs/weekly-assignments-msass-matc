#!/usr/bin/env python3

import requests
import json
import argparse
import bs4
import socket


#res = requests.get("http://172.31.29.252/q2")
#res.raise_for_status
#myHTML = bs4.BeautifulSoup(res.text, features="html.parser")
#print(myHTML.h3)
#print(type(myHTML.H3))
#myH3 = (myHTML.h3)
#print(myH3)
#H3str = str(myH3)
#print(type(H3str))
#output = H3str[8:25:2]
#print(output)

#response = requests.get("http://172.31.29.252/q3")
#headers = response.headers
#print(headers)
#MATC = headers["MATC-HEADER"]
#print(type(MATC))
#print(MATC)
#print(type(headers))
#MATC = f"{headers[MATC_HEADER]}"
#print(MATC)
#for key in headers.keys():
#  print(f"{headers[key]}")

#response = requests.get("http://172.31.29.252/q4")

#print(response.text)

#myDict = json.loads(response.text)
#print(type(myDict))

#print(myDict['The Shining']['publisher'])

#for key in myDict.keys():
#    print(f"{myDict[key][3]['publish_info']['publisher']}")

#print(json.dumps(myDict["Music and Books"]))

print("this is my spoon")

#RHost = '172.31.29.253'
#RPorts = range(5000,6000)

#myTimeout = 2

#for RPort in RPorts:
#    C_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#    C_SOCK.settimeout(myTimeout)
#    try:
#        C_SOCK.connect((RHost,RPort))
#        print(f"Connection State: {RPort}::Port Open")
#        C_SOCK.close()
#    except socket.error as e:
#        print(f"Connection State: {RPort}:: Port closed/filtered")
#        C_SOCK.close()  

remoteHost = '172.31.29.253'
remotePort = 5150

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((remoteHost,remotePort))

clientSocket.send(b"secret")

receivedData = clientSocket.recv(1024)

print(receivedData.decode())

clientSocket.close()

#remoteHost = '172.31.29.253'
#remotePort = 5001

#clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#clientSocket.connect((remoteHost,remotePort))

#clientSocket.send(b"secret")

#receivedData = clientSocket.recv(1024)

#print(receivedData.decode())

#clientSocket.close()