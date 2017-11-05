def getValidInput():
	string = input("Please enter a list of names, seperated by a comma: ")
	for x in string:
		if (x < "A" and x != " " and x != ","):
			return getValidInput()
		if (x > "z"):
			return getValidInput()
		if (x > "Z" and x < "a"):
			return getValidInput()
	
	return string

def printFreq(counter):
	# for letter in counter:
	left = len(counter) - 1
	while (left >= 0):
		print(counter[left][0] + " - " + str(counter[left][1]), end = "")
		if (left != 0):
			print(", ", end = "")
		left -= 1

def main():
	names = getValidInput().upper()

	counter = []

	for x in names:
		if (x == "," or x == " "):
			continue
		
		itemInced = False

		for letter in counter:
			if (letter[0] == x):
				letter[1] += 1
				itemInced = True
				break

		if itemInced:
			continue

		counter.append([x, 1])

	printFreq(counter)

main()
