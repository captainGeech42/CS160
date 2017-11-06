def main():
	input1 = getValidInput("Please enter the first list of integers, seperated by a comma: ")
	input2 = getValidInput("Please enter the second list of integers, seperated by a comma: ")
	
	list1 = sortList(buildList(input1))
	list2 = sortList(buildList(input2))

	print("Same Length: " + ("Yes" if isSameLength(list1, list2) else "No"), end = " | ")

	print("Same Sum: " + ("Yes" if isSameSum(list1, list2) else "No") + " - ", end = '')
	if (isSameSum(list1, list2)):
		print(getSum(list1), end = " | ")
	else:
		print("List 1: " + str(getSum(list1)) + ", List 2: " + str(getSum(list2)), end = " | ")
	
	print("Common Numbers: ", end = '')
	common = getCommonNumbers(list1, list2)
	if (len(common) == 0):
		print("No")
	else:
		print("Yes - ", end = '')
		length = len(common)
		for x in range(length - 1):
			print(str(common[x]), end = ", ")
		print(common[length - 1])

def getValidInput(message):
	string = "B"
	while (not isValidInput(string)):
		string = input(message).strip()
	return string

def isValidInput(string):
	if (string == ""):
		return False
	for char in string:
		if (char < "0" and (char != " " and char != "," and char != "-")):
			return False
		if (char > "9"):
			return False
	return True

def buildList(string):
	newString = ""
	for char in string:
		if (char != " "):
			newString += char

	num = ""
	numList = []
	for char in newString:
		if (char == ","):
			if (num == ""):
				continue
			numList.append(int(num))
			num = ""
		else:
			num += char
	if (num != ""):
		numList.append(int(num))
	return numList

def isSameLength(list1, list2):
	return len(list1) == len(list2)

def getSum(numList):
	sum = 0
	for x in numList:
		sum += x
	return sum

def isSameSum(list1, list2):
	return getSum(list1) == getSum(list2)

def sortList(numList):
	while (not isSorted(numList)):
		for x in range(len(numList) - 1):
			if (numList[x] > numList[x + 1]):
				numList[x] = numList[x] ^ numList[x + 1]
				numList[x + 1] = numList[x] ^ numList[x + 1]
				numList[x] = numList[x] ^ numList[x + 1]
	return numList

def isSorted(numList):
	for x in range(len(numList) - 1):
		if (numList[x] > numList[x + 1]):
			return False
	return True

def getCommonNumbers(list1, list2):
	common = []

	big = []
	small = []
	if (len(list1) > len(list2)):
		big = list1
		small = list2
	else:
		big = list2
		small = list1
	
	for x in big:
		if doesContainNum(small, x):
			if (not doesContainNum(common, x)):
				common.append(x)
	
	return common

def doesContainNum(numList, num):
	for x in numList:
		if (x == num):
			return True
	return False

main()
