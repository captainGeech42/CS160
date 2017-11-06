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
	length = len(counter)
	for x in range(length - 1):
		print(counter[x][0] + " - " + str(counter[x][1]), end = ", ")
	print(counter[length - 1][0] + " - " + str(counter[length - 1][1]))

def sortFreqList(freqList):
	while (not isFreqListSorted(freqList)):
		for x in range(len(freqList) - 1):
			if (freqList[x][0] > freqList[x + 1][0]):
				temp = freqList[x]
				freqList[x] = freqList[x + 1]
				freqList[x + 1] = temp
	return freqList

def isFreqListSorted(freqList):
	for x in range(len(freqList) - 1):
		if (freqList[x][0] > freqList[x + 1][0]):
			return False
	return True

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

	printFreq(sortFreqList(counter))

main()
