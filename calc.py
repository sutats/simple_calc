# Simply python calculator
__author__ = "sutats"
__version__ = "v1.0"

def convertString(str):
	try:
		return int(str)
	except ValueError:
		return float(str)

def add(a, b):
	return convertString(a) + convertString(b)

def subtract(a, b):
	return convertString(a) - convertString(b)

def multiply(a, b):
	return convertString(a) * convertString(b)

def divide(a, b):
	return convertString(a)	/ convertString(b)

keepProgramRunning = True

while keepProgramRunning:
	print '''
*----------------------------------------------*
|  Calculator v1.0                  Coded by:  |      
|                                      sutats  |
|             Choose:                          |
|               1. Add                         |
|               2. Subtract                    |
|               3. Multiply                    |
|               4. Divide                      |
|               5. Quit                        |
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
		print "Bye!"
		keepProgramRunning = False
	else:
		print "Invalid Input\n"