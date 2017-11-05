import pdb

def printBoard(board):
	print("-" * 13)
	for row in board:
		print("| ", end = '')
		for item in row:
			print(item, end = " | ")
		print()
		print("-" * 13)

def generateBoard(size):
	board = []
	for x in range(size):
		board.append([])
		for y in range(size):
			board[x].append(" ")
	return board

def isGameWon(board):
	# check row for same character
	for row in board:
		if (len(set(row)) <= 1):
			if (row[0] != " "):
				return row[0]
	
	# check column for same charcter
	for index in range(len(board)):
		char = board[index][0]
		allEqual = True
		for index2 in range(len(board)):
			for item in board[index]:
				if (item != char):
					allEqual = False
					break
			if (char != " " and allEqual):
				return char

	# check diagonal (TL-BR)
	char = board[0][0]
	allEqual = True
	for index in range(1, len(board)):
		if (board[index][index] != char):
			allEqual = False
	if (allEqual and char != " "):
		return char

	# check diagonal (TR-BL)
	char = board[len(board[0])-1][0]
	
	
	# no winning configurations were found
	return False

def isStalemate(board):
	if (isGameWon(board) == True):
		return False

	for x in board:
		for y in x:
			if (y == " "):
				return False

	return True

def main():
	board = generateBoard(3)
	p1Name = input("Please enter Player 1's name: ")
	p2Name = input("Please enter Player 2's name: ")

	print("Welcome to Tic-Tac-Toe.")
	print(p1Name + " will be X, and " + p2Name + " will be O")
	
	p1Turn = True

	# while ((not isGameWon(board)) and (not isStalemate(board))):
	while ((isGameWon(board) == False) and (isStalemate(board) == False)):
		printBoard(board)

		rowWord = input((p1Name if p1Turn else p2Name)  + ", please choose a row (top, middle, bottom): ")
		row = -1
		if (rowWord == "top"):
			row = 0
		elif (rowWord == "middle"):
			row = 1
		elif (rowWord == "bottom"):
			row = 2
		else:
			print("You entered an invalid row.")
			continue
		
		columnWord = input((p1Name if p1Turn else p2Name) + ", please choose a column (left, middle, right): ")
		column = -1
		if (columnWord == "left"):
			column = 0
		elif (columnWord == "middle"):
			column = 1
		elif (columnWord == "right"):
			column = 2
		else:
			print("You entered an invalid column.")
			continue
		
		if (board[row][column] != " "):
			print("This space is already filled.")
			continue

		board[row][column] = "X" if p1Turn else "O"

		p1Turn = not p1Turn

	printBoard(board)

	if (isStalemate(board)):
		print("Stalemate!")
	elif (isGameWon(board) == "X"):
		print(p1Name + " wins!")
	elif (isGameWon(board) == "O"):
		print(p2Name + " wins!")
	else:
		print("error")
	
main()
