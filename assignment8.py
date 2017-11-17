'''
TODO: Functions that do not currently support a NxN board:
 - getGameCoordinates
 - printBoard

INFO:
 - X = black
 - O = white
 - board is accessed with board[row][col]
'''

def main():
	board = generateBoard(8)
	p1Name = input("Please enter Player 1's name: ")
	p2Name = input("Please enter Player 2's name: ")

	print("Welcome to Othello.")
	print(p1Name + " will be X, and " + p2Name + " will be O")

	p1Turn = True

	while (not isGameOver(board)):
		printBoard(board)

		row = 0
		col = 0
		while True:
			row, col = getGameCoordinates(p1Name if p1Turn else p2Name)
			if (isValidMove(board, row, col)):
				break
			print("The coordinates are invalid.")

		board[row][col] = "X" if p1Turn else "O"

		flipPieces(board, row, col)

		p1Turn = not p1Turn

	printBoard(board)

	winner = getWinner(board)
	if (winner == "tie"):
		print("It's a tie!")
	elif (winner == "white"):
		print(p2Name + " wins!")
	elif (winner == "black"):
		print(p1Name + " wins!")
	else:
		print("rip idek")

def checkDown(board, row, col):
	n = len(board)
	origin = board[row][col]
	if (row == n - 1):
		return False
	char = board[row + 1][col]
	if (char == origin or char == " "):
		return False
	for x in range(row + 2, n - row):
		char = board[x][col]
		if (char != origin and char != " "):
			return True
	return False

def checkDownLeft(board, row, col):
	# subtract from the column, add to the row
	n = len(board)
	origin = board[row][col]
	if (row == n - 1 or col == 0):
		return False
	char = board[row + 1][col - 1]
	if (char == origin or char == " "):
		return False
	for x in range(1, min(n - row, col)):
		char = board[row + x][col - x]
		if (char == origin):
			return True
	return False

def checkDownRight(board, row, col):
	# add to the column and the row
	n = len(board)
	origin = board[row][col]
	if (row == n - 1 or col == n - 1):
		return False
	char = board[row + 1][col + 1]
	if (char == origin or char == " "):
		return False
	for x in range(1, min(n + row, n + col)):
		char = board[row + x][col + x]
		if (char == origin):
			return True
	return False

def checkLeft(board, row, col):
	n = len(board)
	origin = board[row][col]
	if (col == 0):
		return False
	char = board[row][col - 1]
	if (char == origin or char == " "):
		return False
	for x in range(col - 2, n - col, -1):
		char = board[row][x]
		if (char == origin):
			return True
	return False

def checkRight(board, row, col):
	n = len(board)
	origin = board[row][col]
	if (col == n - 1):
		return False
	char = board[row][col + 1]
	if (char == origin or char == " "):
		return False
	for x in range(col + 2, n - col):
		char = board[row][x]
		if (char != origin and char != " "):
			return True
	return False

def checkUp(board, row, col):
	n = len(board)
	origin = board[row][col]
	if (row == 0):
		return False
	char = board[row - 1][col]
	if (char == origin or char == " "):
		return False
	for x in range(row - 2, n - row, -1):
		char = board[x][col]
		if (char != origin and char != " "):
			return True
	return False

def checkUpLeft(board, row, col):
	# subtract from the column and the row
	n = len(board)
	origin = board[row][col]
	if (row == 0 or col == 0):
		return False
	char = board[row - 1][col - 1]
	if (char == origin or char == " "):
		return False
	for x in range(1, min(n - row, n - col)):
		char = board[row - x][col - x]
		if (char == origin):
			return True
	return False

def checkUpRight(board, row, col):
	# add to the column, subtract from the row
	n = len(board)
	origin = board[row][col]
	if (col == n - 1 or row == 0):
		return False
	char = board[row - 1][col + 1]
	if (char == origin or char == " "):
		return False
	for x in range(1, min(n - col, row)):
		char = board[row - x][col + x]
		if (char == origin):
			return True
	return False

def flipPieces(board, row, col):
	origin = board[row][col]

	if (checkDown(board, row, col)):
		inc = 1
		while (board[row + inc][col] != origin):
			board[row + inc][col] = origin
			inc += 1

	if (checkUp(board, row, col)):
		inc = 1
		while (board[row - inc][col] != origin):
			board[row - inc][col] = origin
			inc += 1

	if (checkRight(board, row, col)):
		inc = 1
		while (board[row][col + inc] != origin):
			board[row][col + inc] = origin
			inc += 1

	if (checkLeft(board, row, col)):
		inc = 1
		while (board[row][col - inc] != origin):
			board[row][col - inc] = origin
			inc += 1

	if (checkDownLeft(board, row, col)):
		inc = 1
		while (board[row + inc][col - inc] != origin):
			board[row + inc][col - inc] = origin
			inc += 1

	if (checkUpLeft(board, row, col)):
		inc = 1
		while (board[row - inc][col - 1] != origin):
			board[row - inc][col - 1] = origin
			inc += 1

	if (checkDownRight(board, row, col)):
		inc = 1
		while (board[row + 1][col + inc] != origin):
			board[row + 1][col + inc] = origin
			inc += 1

	if (checkUpRight(board, row, col)):
		inc = 1
		while (board[row - inc][col + inc] != origin):
			board[row - inc][col + inc] = origin
			inc += 1

def generateBoard(n):
	# build empty board
	board = []
	for x in range(n):
		board.append([])
		for y in range(n):
			board[x].append(" ")

	# insert starting pieces
	middle = (n // 2) - 1
	board[middle][middle] = "O"
	board[middle + 1][middle + 1] = "O"
	board[middle + 1][middle] = "X"
	board[middle][middle + 1] = "X"

	return board

def getGameCoordinates(player):
	# NOTE: This currently does not support an N x N board

	column = "B"
	while True:
		column = input(player + ", please input your column selection (a-h): ").lower()
		if (column < "a" or column > "h"):
			print("Invalid column entered.")
			continue
		break

	row = "B"
	while True:
		row = input(player + ", please input your row selection (1-8): ")
		if (row < "1" or row > "8"):
			print("Invalid row entered.")
			continue
		break
	
	# return (ord(column) - 97, int(row))
	return (int(row) - 1, ord(column) - 97)

def getWinner(board):
	whiteCounter = 0
	blackCounter = 0
	n = len(board)
	for x in range(n):
		for y in range(n):
			char = board[x][y]
			if (char == "O"):
				whiteCounter += 1
			elif (char == "X"):
				blackCounter += 1
	if (whiteCounter == blackCounter):
		return "tie"
	elif (whiteCounter > blackCounter):
		return "white"
	else:
		return "black"

def isGameOver(board):
	n = len(board)
	for x in range(n):
		for y in range(n):
			if (isValidMove(board, x, y)):
				return False
	return True

def isValidMove(board, row, col):
	if (board[row][col] != " "):
		return False

	if (checkLeft(board, col, row) or
		checkUpLeft(board, col, row) or
		checkUp(board, col, row) or
		checkUpRight(board, col, row) or
		checkRight(board, col, row) or
		checkDownRight(board, col, row) or
		checkDown(board, col, row) or
		checkDownLeft(board, col, row)):
		return True

def printBoard(board):
	# NOTE: This function does not support an NxN board
	n = len(board)
	divider = "  " + ("-" * (n + (2 * n) + n + 1))
	print("    a   b   c   d   e   f   g   h")
	print(divider)
	label = 1
	for row in board:
		print(str(label) + " | ", end = '')
		for item in row:
			print(item, end = " | ")
		print()
		print(divider)
		label += 1

main()