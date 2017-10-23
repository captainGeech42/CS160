firstRun = True
while True:
	# choose the mod
	mode = input("Please select 'scientific' or 'programmer' mode: " if firstRun else "Please select next mode, or 'exit' to quit the calculator: ")

	if (mode == "scientific"):
		# scientific mode

		validOperations = ["+", "-", "*", "/", "**"]
		chosenOperation = ""
		exponent = False

		chosenOperation = input("Please pick an operation (+, -, *, /, **): ")

		while chosenOperation not in validOperations:
			chosenOperation = input("Please choose a valid operation: ")

		if chosenOperation == "**":
			exponent = True

		try:
			num1 = float(input("Please enter the first operand: " if not exponent else "Please enter the base: "))
			num2 = float(input("Please enter the second operand: " if not exponent else "Please enter the exponent: "))
			
			if (chosenOperation == "+"):
				print("The sum is " + str(num1 + num2))
			elif (chosenOperation == "-"):
				print("The difference is " + str(num1 - num2))
			elif (chosenOperation == "*"):
				print("The product is " + str(num1 * num2))
			elif (chosenOperation == "/"):
				if (num2 == 0):
					print("You can not divide by zero.")
					continue
				print("The quotient is " + str(num1 / num2))
			elif (chosenOperation == "**"):
				print("The result of the exponentiation is " + str(num1**num2))
			else:
				print("Please enter a valid operator")
		except ValueError:
			print("Please enter a valid float for " + ("each operand" if not exponent else "the base/exponent"))

	elif (mode == "programmer"):
		# programmer mode
		
		decimalNumber = 0
		try:
			decimalNumber = int(input("Decimal number: "))
			if (decimalNumber < 0):
				raise ValueError()
			numBits = 1
			tempDiv = decimalNumber
			while tempDiv // 2 > 0:
				numBits += 1
				tempDiv = tempDiv // 2
			
			binaryNumber = ""
			for bit in range(numBits - 1, -1, -1):
				test = decimalNumber - 2 ** bit
				if (test >= 0):
					binaryNumber += "1"
					decimalNumber = test
				else:
					binaryNumber += "0"
	
			print("Your binary number is " + str(binaryNumber))
		except ValueError:
			print("Please enter a valid positive integer")
		
	elif (mode == "exit"):
		exit()
	else:
		print("Invalid mode specified")

	firstRun = False
