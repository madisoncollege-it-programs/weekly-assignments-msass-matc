#!/usr/bin/env python3

import socket
RHOST = '127.0.0.1'
RPORT = 5000
RCV_DATA = ''

C_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

timeout = 5
C_SOCK.settimeout(timeout)
try:
    C_SOCK.connect((RHOST, RPORT))
    SND_DATA = "Hello."
    while SND_DATA!= "exit":
        SND_DATA = input("What message would you like to send?:")
        C_SOCK.send(bytearray(SND_DATA,'utf8'))
        print("Yay, we connected!")
        RCV_DATA = C_SOCK.recv(1024)
    print(RCV_DATA.decode())
except socket.error as e:
    print(f"connection stsatus : {RHOST}:{RPORT} is {e}")
C_SOCK.close()
