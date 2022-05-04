#!/usr/bin/env python3

import c2f
import f2c

print("What would you like to convert?\n1.Fahrenheit to Celcius\n2.Celcius to Fahrenheit")
var_measure = input("->") 
print(var_measure)

var_temp = input("Please input the temperature you would like to convert:")
print(var_temp)

var_temp = int(var_temp)

if var_measure == "1":
    var_temp = f2c.fahr_to_cels(var_temp)
    print(var_temp)
elif var_measure == "2":
    var_temp = c2f.cels_to_fahr(var_temp)
    print(var_temp)