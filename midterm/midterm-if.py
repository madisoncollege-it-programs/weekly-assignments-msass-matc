#!/usr/bin/env python3
print("Name: Meaghan Sass")

mylist = ["gmeach18@ed.gov","248.253.63.149","Whiteland","80.222.19.190","Kayley","dcassyqw@microsoft.com"]

hFile = open("Midterm-if.txt","r")

total = 0

for line in hFile:
    #print(line)
    for keywords in mylist:
        #print(keywords)
        if keywords in line:
           #print(line)
           newlist = line.split(',')
           newlisttwo = newlist[0]
           #print(newlisttwo)
           newlistthree = int(newlisttwo)
           #print(newlistthree)
           total += newlistthree
           print(f"The total is:{total}")
             
hFile.close()