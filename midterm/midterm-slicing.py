#!/usr/bin/env python3
print("Name: Meaghan Sass")

hFile = open("slicing-file.txt","r")
varWords = hFile.readlines()
first = varWords[24:25:]
second = varWords[2:5:]
third = varWords[-10:11:-2]
fourth = varWords[10:13:]
fifth = varWords[8:5:-1]

varFirst = " ".join(first)
varSecond = " ".join(second)
varThird = " ".join(third)
varFourth = " ".join(fourth)
varFifth = " ".join(fifth)

quote = " ".join([varFirst, varSecond, varThird, varFourth, varFifth])
quotetwo = quote.replace('\n', ' ')

print(quotetwo)

hFile.close()

