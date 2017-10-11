decNum = int(input("Decimal Number?\n"))

if (decNum > 255 or decNum < 0):
	print("Invalid number given. Please enter an integer between 0 and 255")
else:
	b7 = decNum // 128
	if (b7 == 1):
		decNum = decNum - 128
	
	b6 = decNum // 64
	if (b6 == 1):
		decNum = decNum - 64

	b5 = decNum // 32
	if (b5 == 1):
		decNum = decNum - 32

	b4 = decNum // 16
	if (b4 == 1):
		decNum = decNum - 16

	b3 = decNum // 8
	if (b3 == 1):
		decNum = decNum - 8

	b2 = decNum // 4
	if (b2 == 1):
		decNum = decNum - 4

	b1 = decNum // 2
	if (b1 == 1):
		decNum = decNum - 2

	b0 = decNum // 1

	num = str(b7) + str(b6) + str(b5) + str(b4) + str(b3) + str(b2) + str(b1) + str(b0)

	print("Binary number is " + num)
