#!/usr/bin/env python3
import subprocess

myProc = subprocess.run(['ps', '-axco', 'command'],stdout=subprocess.PIPE)
myProcString = myProc.stdout.decode().split('\n')

for line in myProcString:
    print(line)
print(len(myProcString[1::]))