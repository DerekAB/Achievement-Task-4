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

decision = input("Would you like to convert temperature or speed: \n Temperature [1] \n Speed [2] \n").strip()

if decision == 1:
    print('You have selected Temperature.')
    
