#!/usr/bin/env python3

def cels_to_fahr(degrees_celcius):
     degrees_celcius = int(degrees_celcius)
     degrees_fahrenheit = ((degrees_celcius *9/5) + 32)
     return degrees_fahrenheit
#print(cels_to_fahr(degrees_fahrenheit))

def main():
    degrees_celcius = input("Enter the number you wish to convert to fahrenheit:")
    degrees_fahrenheit = cels_to_fahr(degrees_celcius)
    print(degrees_fahrenheit)

if __name__ == "__main__":
    main()
    