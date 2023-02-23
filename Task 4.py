#Name:                  Task 4.py
#Author:                Derek Baker
#Date Created:          23-02-2023
#Date Last Modified:    23-02-2023
#
#Purpose:
#
#The purpose of this program is to convert temperature and speed
#into the desired unit. The program will first ask if they want
#to convert speed or temperature, then ask if they want to convert
#from Celcius to Fahrenheit or vice versa, or if they want to 
#from KPH to MPH or vice versa.

def temperature(unit, number):
    global conversion 
    if unit == 'c':
        conversion = (number * 1.8) + 32
        roundedConversion = round(conversion, 2)
        print(str(roundedConversion) + ' F')
        return True
    
    
    if unit == 'f':
        conversion = (number - 32) * 0.5556
        roundedConversion = round(conversion, 2)
        print(str(roundedConversion) + ' C')
        return True
        
        

decision = float(input("Would you like to convert temperature or speed: \n Temperature [1] \n Speed [2] \n"))

if decision == 1:
    unit = input("What is the unit you are converting from? 'C' for Celcius or 'F' for Fahrenheit:  ").strip().lower()
    number = int(input("What is the temperature?: "))
    temperature(unit, number)
    
if decision == 2:
    unit = input("What is the unit you are converting from? 'KPH' for Kilometers Per Hour to Miles Per Hour, or 'MPH' for Miles Per Hour to Kilometers Per Hour: ").strip().lower()
    
    
