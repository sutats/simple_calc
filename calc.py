# Simply python calculator
__author__ = "sutats"
__version__ = "v1.2"

import sys

# Converts string to int or float
def convertString(str):
	try:
		return int(str)
	except ValueError:
		return float(str)

def add(a, b): # Addition function etc..
	return convertString(a) + convertString(b)

def subtract(a, b):
	return convertString(a) - convertString(b)

def multiply(a, b):
	return convertString(a) * convertString(b)

def divide(a, b):
	return convertString(a)	/ convertString(b)

def exponent(a, b):
	return convertString(a) ** convertString(b)

def force(a, b):  					# Used this so it prints on the same line
	sys.stdout.write('Force(N) = ') # There's probably a better way but I'm learning
									
	return convertString(a) * convertString(b)

def physicsMenu(): # Defines the secondary menu for physics calculations
	print '''	   
*--------------------------------------*
|                                      |
|             1. Force (F=ma)          |
|                                      |
|                                      |
|                                      |
|                                      |
|                                      |
*--------------------------------------*
'''
	choice = raw_input("> ")
	if choice == "1":
		a = raw_input("Mass(kg): ")
		b = raw_input("Acceleration: ")
		print float(force(a, b))
	else:
		print "Invalid Input"


keepProgramRunning = True

while keepProgramRunning:  # Main calculator menu
	print '''
*----------------------------------------------*
|  Calculator v1.1                  Coded by:  |      
|                                      sutats  |
|                                              |
|             Choose:                          |
|               1. Add                         |
|               2. Subtract                    |
|               3. Multiply                    |
|               4. Divide                      |
|               5. Exponent                    |
|               6. Physics Calculations        |
|               7. Quit                        |
|                                              |
*----------------------------------------------*
'''

	choice = raw_input("Enter choice: ")

	if choice == "1":
		a = raw_input("A: ")
		b = raw_input("B: ")
		print add(a, b)

	elif choice == "2":
		a = raw_input("A: ")
		b = raw_input("B: ")
		print subtract(a, b)

	elif choice == "3":
		a = raw_input("A: ")
		b = raw_input("B: ")
		print multiply(a, b)

	elif choice == "4":
		a = raw_input("A: ")
		b = raw_input("B: ")
		while b == "0":
			print "Invalid Number!"
			b = raw_input("B: ")
		print float(divide(a, b))

	elif choice == "5":
		a = raw_input("A: ")
		b = raw_input("B: ")
		print exponent(a, b)

	elif choice == "6":
		physicsMenu()

	elif choice == "7":
		print "Bye!"
		keepProgramRunning = False