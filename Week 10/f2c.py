#!/usr/bin/env python3

def fahr_to_cels(degrees_fahrenheit):
     degrees_fahrenheit = int(degrees_fahrenheit)
     degrees_celcius = ((degrees_fahrenheit - 32)* 5/9)
     return degrees_celcius
#print(fahr_to_cels(degrees_fahrenheit))

def main():
    degrees_fahrenheit = input("Enter the number you wish to convert to celcius:")
    degrees_celcius = fahr_to_cels(degrees_fahrenheit)
    print(degrees_celcius)

if __name__ == "__main__":
    main()




