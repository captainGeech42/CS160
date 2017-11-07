def main():
	function = ""
	while True:
		string = input("Please enter the name of the function to be tested (in the correct casing)" + (": " if function == "" else ", press <enter> to continue testing the previous function (" + function + "), or 'exit': "))
		if (string != ""):
			function = string

		if (function == "isPositive"):
			printFuncReturn(isPositive(getStringArgument()))
		elif (function == "isDecimal"):
			printFuncReturn(isDecimal(getStringArgument()))
		elif (function == "inBound"):
			print("in progress...")
		elif (function == "capitalsPresent"):
			printFuncReturn(capitalsPresent(getStringArgument()))
		elif (function == "numbersPresent"):
			printFuncReturn(numbersPresent(getStringArgument()))
		elif (function == "isEven"):
			printFuncReturn(isEven(getStringArgument()))
		elif (function == "isOdd"):
			printFuncReturn(isOdd(getStringArgument()))
		elif (function == "isCorrectLength"):
			string = input("Please enter the string argument: ")
			lenght = input("Please enter the length argument: ")
			printFuncReturn(isCorrectLength(string, length))
		elif (function == "exit"):
			exit()
		else:
			print("An unrecognized function was given.")

def getStringArgument():
	return input("Please enter the string argument: ")

def printFuncReturn(ret):
	print("The function returned: " + str(ret))

def isPositive(string):
	# check for any values that are not between 0 and 9
	for char in string:
		if (char < "0" or char > "9"):
			return False

	# check for length of 1 and string is "0"
	if (string == "0"):
		return False

	return True

def isDecimal(string):
	# check for any values that are not between 0 and 9, or . or -
	for char in string:
		if ((char < "0" and (char != "." and char != "-")) or char > "9"):
			return False

	return True

def inBound():
	# wut
	

	return True

def capitalsPresent(string):
	# check each character if it is between A and Z
	for char in string:
		if (char >= "A" and char <= "Z"):
			return True

	return False

def numbersPresent(string):
	# check each character if it is between 0 and 9
	for char in string:
		if (char >= "0" and char <= "9"):
			return True

	return False

def isEven(string):
	if (not isPositive(string)):
		return False
	
	# check if last character is 0, 2, 4, 6, or 8
	if (string[-1:] == "0" or
		string[-1:] == "2" or
		string[-1:] == "4" or
		string[-1:] == "6" or
		string[-1:] == "8"):
		return True

	return False

def isOdd(string):
	if (not isPositive(string)):
		return False
	
	# check if last character is 1, 3, 5, 7, or 9
	if (string[-1:] == "1" or
		string[-1:] == "3" or
		string[-1:] == "5" or
		string[-1:] == "7" or
		string[-1:] == "9"):
		return True

	return False

def isCorectLength(string, length):
	if (not isPositive(length)):
		return False
	
	# for loop to get length of the string
	strLength = 0
	for char in string:
		strLength += 1

	return strLength == length

main()
