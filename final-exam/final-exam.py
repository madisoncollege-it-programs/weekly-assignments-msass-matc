#!/usr/bin/env python3

import requests
import json
import argparse
import bs4
import socket

parser = argparse.ArgumentParser(description='creating a parser to add arguments')
    
parser.add_argument('-i', '--ipaddress', dest='myIP', type=str, required=True, help='Enter an IP address')
parser.add_argument('-f', '--function', dest='myFunc', type=int, required=True, help='Enter a function number')

myIP = parser.parse_args().myIP
myFunc = parser.parse_args().myFunc

#print(myIP)
#print(myFunc)

URL = (f"http://{myIP}/q{myFunc}")

print(f"Meaghan Sass")
print(URL)

def get_response():
    response = requests.get(URL)
    return response.text

def parse_string():
    res = requests.get(URL)
    res.raise_for_status
    myHTML = bs4.BeautifulSoup(res.text, features="html.parser")
    #print(myHTML.h3)
    #print(type(myHTML.H3))
    myH3 = (myHTML.h3)
    #print(myH3)
    H3str = str(myH3)
    #print(type(H3str))
    H3sliced = H3str[8:25:2]
    output = (f"Answer: {H3sliced} Meaghan Sass")
    return output

def parse_header():
    response = requests.get(URL)
    headers = response.headers
    MATC = headers["MATC-HEADER"]
    return MATC
    
def parse_json():
    response = requests.get(URL)
    myDict = json.loads(response.text)
    for key in myDict.keys():
        print(f"{myDict[key][3]['publish_info']['publisher']}")

def socket_client():
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

    remoteHost = f"{myIP}"
    remotePort = 5150

    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((remoteHost,remotePort))

    clientSocket.send(b"secret")

    receivedData = clientSocket.recv(1024)

    print(receivedData.decode())

    clientSocket.close()

if myFunc == 1:
    Answer1 = get_response()
    print(Answer1)

if myFunc == 2:
    Answer2 = parse_string()
    print(Answer2)

if myFunc == 3:
    Answer3 = parse_header()
    print(Answer3)

if myFunc == 4:
    Answer4 = parse_json()
    print(Answer4)

if myFunc == 5:
    Answer5 = socket_client()
    print(Answer5)

else:
    print("Oops...")



