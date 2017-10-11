decNum = int(input("Decimal Number?\n"))

b7 = decNum // 128
decNum = decNum - (b7 * 128)

b6 = decNum // 64
decNum = decNum - (b6 * 64)

b5 = decNum // 32
decNum = decNum - (b5 * 32)

b4 = decNum // 16
decNum = decNum - (b4 * 16)

b3 = decNum // 8
decNum = decNum - (b3 * 8)

b2 = decNum // 4
decNum = decNum - (b2 * 4)

b1 = decNum // 2
decNum = decNum - (b1 * 2)

b0 = decNum // 1

num = str(b7) + str(b6) + str(b5) + str(b4) + str(b3) + str(b2) + str(b1) + str(b0)

print("Binary number is " + num)
