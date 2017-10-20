import math

# choose mode
firstRun = True
while True:
	mode = input("Please select 'scientific' or 'programmer' mode: " if firstRun else "Please select next mode, or 'exit' to quit the calculator: ")
	if (mode == "scientific"):
		#scientific mode

		operation = input("Please pick an operator (+, -, *, /, or **): ")
		num1 = float(input("Please enter the first operand: "))
		num2 = float(input("Please enter the second operand: "))
		
		if (operation == "+"):
			print("The sum is " + str(num1 + num2))
		elif (operation == "-"):
			print("The difference is " + str(num1 - num2))
		elif (operation == "*"):
			print("The product is " + str(num1 * num2))
		elif (operation == "/"):
			print("The quotient is " + str(num1 / num2))
		elif (operation == "**"):
			print("The result of the exponentiation is " + str(num1**num2))
		else:
			print("Please enter a valid operator")
	elif (mode == "programmer"):
		#programmer mode

		decimalNumber = math.fabs(int(input("Decimal number: ")))
		# since we only want unsigned decimal numbers, if the number is negative, we can drop the sign
		numBits = 1
		tempDiv = decimalNumber
		while True:
			if (tempDiv // 2 > 0):
				numBits += 1
				tempDiv = tempDiv // 2
			else:
				break
		
		binaryNumber = ""
		for bit in range(numBits - 1, -1, -1):
			test = decimalNumber - 2**bit
			if (test >= 0):
				binaryNumber += "1"
				decimalNumber = test
			else:
				binaryNumber += "0"

		print("Your binary number is " + str(binaryNumber))
	elif (mode == "exit"):
		exit()
	else:
		print("Invalid mode specified")

	firstRun = False
