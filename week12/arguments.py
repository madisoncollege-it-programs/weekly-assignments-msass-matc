#!/usr/bin/env python3

import argparse

myParser = argparse.ArgumentParser(description="This is Meaghan's script")
myParser.add_argument('-m',dest='BASIC', default= "Text", type=str, help="Enter some text")
myParser.add_argument('-i', "--integer", dest="integer", type=int, required=True, metavar='[an integer]', help="<required> Enter a simple Integer")
myParser.add_argument('-d', "--float", dest="float", type=float, metavar='[a float]', help="Enter a simple float")
myParser.add_argument('-s', "--string", dest="string", type=str, metavar='[a string]', help="Enter a simple string")
myParser.add_argument('-l', dest="strings", nargs='+', metavar='[strings]', help="Enter a list of strings (space delimited)")
myParser.add_argument('-t', '--set-true', action='store_true', help="Toggle from default False to True")
myParser.add_argument('-f', '--setfalse', action='store_false', help="Toggle from default True to False")
myParser.add_argument('-v', '--version', dest='version', action='version', help="show program's version number and exit")

print(myParser.parse_args())
