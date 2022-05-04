#!/usr/bin/env python3
hFile = open("/etc/passwd","r")
strfiletext = hFile.read()
print(len(strfiletext))
print("the len() function gives you the length of the file, in this case the number of characters")
print("you would use this read function over other read functions when you can read the whole file and you would like to know the number of characters")
hFile.close()
hFile = open("/etc/passwd","r")
listfiletext = hFile.readlines()
print(len(listfiletext))
print("the len() function gives you the length of the file, in this case because the data type is a list, it will give the number of lines")
print("you would use this read function over other read functions when you can read the whole file and would like to know the number of lines")
hFile.close()
count = 0
hFile = open("/etc/passwd","r")
for line in hFile:
    count += len(line)
print(count)
print("You would use this read function over other read functions when you have a large file that you cannot read all at once")


