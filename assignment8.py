'''
TODO: Functions that do not currently support a NxN board:
 - getGameCoordinates
 - printBoard

INFO:
 - X = black = player1
 - O = white = player2
 - board is accessed with board[row][col]
'''

import sys

def main():
	if (len(sys.argv) != 2):
		print("Too many/little command line arguments. Syntax is: assignment8.py [board size]")
		exit()

	boardSize = sys.argv[1]
	if (boardSize != "8"):
		print("An invalid board size was received. Exiting...")
		exit()

	boardSize = int(boardSize)

	winCounter = [0, 0] #p1, p2

	while True:
		board = generateBoard(boardSize)
		p1Name = input("Please enter Player 1's name: ")
		p2Name = input("Please enter Player 2's name: ")
	
		print("Welcome to Othello.")
		print(p1Name + " will be X, and " + p2Name + " will be O")
	
		p1Turn = True
	
		p1CantPlay = False
		p2CantPlay = False
	
		while (not p1CantPlay and not p2CantPlay):
			printBoard(board)
	
			row = 0
			col = 0
			while True:
				row, col = getGameCoordinates(p1Name if p1Turn else p2Name)
				
				if (isValidMove(board, row, col, "X" if p1Turn else "O")):
					break
				print("The coordinates are invalid.")
	
			board[row][col] = "X" if p1Turn else "O"
	
			flipPieces(board, row, col, ("X" if p1Turn else "O"))
	
			if (p1Turn):
				p1CantPlay = isGameOver(board, "X")
			else:
				p2CantPlay = isGameOver(board, "O")
	
			p1Turn = not p1Turn
	
		printBoard(board)
	
		winner = getWinner(board)
		if (winner == "tie"):
			print("It's a tie!")
		elif (winner == "black"):
			print(p1Name + " wins!")
			winCounter[0] += 1
		elif (winner == "white"):
			print(p2Name + " wins!")
			winCounter[1] += 1
		else:
			print("rip idek")

		again = input("Do you want to play again? ").lower()
		while (again != "yes" and again != "no"):
			print("Unrecognized input.")
			again = input("Do you want to play again? ").lower()

		if (again == "no"):
			break

	print ("Player 1 has won " + winCounter[0] + " times, and Player 2 has won " + winCounter[1] + " times. Thanks for playing!")

def checkDown(board, row, col, origin):
	n = len(board)
	if (row == n - 1):
		return False
	char = board[row + 1][col]
	if (char == origin or char == " "):
		return False
	for x in range(row + 1, n):
		char = board[x][col]
		if (char == " "):
			return False
		if (char == origin):
			return True
	return False

def checkDownLeft(board, row, col, origin):
	n = len(board)
	if (row == n - 1 or col == 0):
		return False
	char = board[row + 1][col - 1]
	if (char == origin or char == " "):
		return False
	for x in range(1, min(n - row, col)):
		char = board[row + x][col - x]
		if (char == " "):
			return False
		if (char == origin):
			return True
	return False

def checkDownRight(board, row, col, origin):
	n = len(board)
	if (row == n - 1 or col == n - 1):
		return False
	char = board[row + 1][col + 1]
	if (char == origin or char == " "):
		return False
	for x in range(1, min(n - row, n - col)):
		char = board[row + x][col + x]
		if (char == " "):
			return False
		if (char == origin):
			return True
	return False

def checkLeft(board, row, col, origin):
	n = len(board)
	if (col == 0):
		return False
	char = board[row][col - 1]
	if (char == origin or char == " "):
		return False
	for x in range(col - 1, 0, -1):
		char = board[row][x]
		if (char == " "):
			return False
		if (char == origin):
			return True
	return False

def checkRight(board, row, col, origin):
	n = len(board)
	if (col == n - 1):
		return False
	char = board[row][col + 1]
	if (char == origin or char == " "):
		return False
	for x in range(col + 1, n):
		char = board[row][x]
		if (char == " "):
			return False
		if (char == origin):
			return True
	return False

def checkUp(board, row, col, origin):
	n = len(board)
	if (row == 0):
		return False
	char = board[row - 1][col]
	if (char == origin or char == " "):
		return False
	for x in range(row - 1, 0, -1):
		char = board[x][col]
		if (char == " "):
			return False
		if (char == origin):
			return True
	return False

def checkUpLeft(board, row, col, origin):
	n = len(board)
	if (row == 0 or col == 0):
		return False
	char = board[row - 1][col - 1]
	if (char == origin or char == " "):
		return False
	for x in range(1, min(n - row, n - col)):
		char = board[row - x][col - x]
		if (char == " "):
			return False
		if (char == origin):
			return True
	return False

def checkUpRight(board, row, col, origin):
	n = len(board)
	if (col == n - 1 or row == 0):
		return False
	char = board[row - 1][col + 1]
	if (char == origin or char == " "):
		return False
	for x in range(1, min(n - col, row)):
		char = board[row - x][col + x]
		if (char == " "):
			return False
		if (char == origin):
			return True
	return False

def flipPieces(board, row, col, origin):
	n = len(board)

	if (checkDown(board, row, col, origin)):
		inc = 1
		while (row + inc < n and board[row + inc][col] != origin and board[row + inc][col] != " "):
			board[row + inc][col] = origin
			inc += 1

	if (checkUp(board, row, col, origin)):
		inc = 1
		while (row - inc >= 0 and board[row - inc][col] != origin and board[row - inc][col] != " "):
			board[row - inc][col] = origin
			inc += 1

	if (checkRight(board, row, col, origin)):
		inc = 1
		while (col + inc < n and board[row][col + inc] != origin and board[row][col + inc] != " "):
			board[row][col + inc] = origin
			inc += 1

	if (checkLeft(board, row, col, origin)):
		inc = 1
		while (col - inc >= 0 and board[row][col - inc] != origin and board[row][col - inc] != " "):
			board[row][col - inc] = origin
			inc += 1

	if (checkDownLeft(board, row, col, origin)):
		inc = 1
		while (row + inc < n and col - inc >= 0 and board[row + inc][col - inc] != origin and board[row + inc][col - inc] != " "):
			board[row + inc][col - inc] = origin
			inc += 1

	if (checkUpLeft(board, row, col, origin)):
		inc = 1
		while (row - inc >= 0 and col - inc >= 0 and board[row - inc][col - inc] != origin and board[row - inc][col - inc] != " "):
			board[row - inc][col - inc] = origin
			inc += 1

	if (checkDownRight(board, row, col, origin)):
		inc = 1
		while (row + inc < n and col + inc < n and board[row + inc][col + inc] != origin and board[row + inc][col + inc] != " "):
			board[row + inc][col + inc] = origin
			inc += 1

	if (checkUpRight(board, row, col, origin)):
		inc = 1
		while (row - inc >= 0 and col + inc < n and board[row - inc][col + inc] != origin and board[row - inc][col + inc] != " "):
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

def isGameOver(board, piece):
	n = len(board)
	for x in range(n):
		for y in range(n):
			if (isValidMove(board, x, y, piece)):
				return False
	return True

def isValidMove(board, row, col, piece):
	if (board[row][col] != " "):
		return False

	if (checkLeft(board, row, col, piece) or
		checkUpLeft(board, row, col, piece) or
		checkUp(board, row, col, piece) or
		checkUpRight(board, row, col, piece) or
		checkRight(board, row, col, piece) or
		checkDownRight(board, row, col, piece) or
		checkDown(board, row, col, piece) or
		checkDownLeft(board, row, col, piece)):
		return True

def printBoard(board):
	# NOTE: This function does not support an N x N board
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