import turtle, math

def main():
	firstRun = True
	
	while True:
		mode = input("Please select star or name: " if firstRun else "Please select star, name, or exit: ").lower()
		
		if (mode == "star"):
			# star stuff
			clearScreen()
			turtle.onclick(star, add = False)
	
		elif (mode == "name"):
			# name stuff
			clearScreen()
			turtle.onclick(name, add = False)

		elif (mode == "exit"):
			exit()
	
		else:
			# mode is invalid
			print("An invalid operation was specified")
	
		if firstRun:
			firstRun = False
		
		# window.mainloop()

def star(x, y):
	clearScreen()
	lineLength = 150
	angle = 36

	for x in range(5):
		turtle.forward(lineLength)
		turtle.right(180 - angle)

def name(x, y):
	clearScreen()
	
	# position turtle
	turtle.penup()
	turtle.setx(-400)
	turtle.sety(400)
	turtle.pendown()

	# Z
	turtle.forward(150)
	turtle.right(180 - 45)
	turtle.forward(150 * math.sqrt(2))
	turtle.left(180 - 45)
	turtle.forward(150)

	# position turtle
	turtle.penup()
	turtle.forward(30)
	turtle.pendown()
	
	# A
	a = math.sqrt(150**2 + 30**2)
	turtle.left(90 - 20)
	turtle.forward(a)
	turtle.right(180 - 40)
	turtle.forward(a)
	
	turtle.penup()	
	line = 2 * (((a / 2) * math.sin(math.radians(20))) / math.sin(math.radians(90)))
	turtle.right(180)
	turtle.forward(a / 2)
	turtle.left(70)
	turtle.pendown()
	turtle.forward(line)
	
	# position turtle
	turtle.penup()
	turtle.right(180)
	turtle.forward(line)
	turtle.right(70)
	turtle.forward(a / 2)
	turtle.left(70)
	turtle.forward(30)
	turtle.pendown()

	# N
	turtle.left(90)
	turtle.forward(150)
	turtle.right(180 - 25)
	turtle.forward(150 / math.sin(math.radians(65)))
	turtle.left(180 - 25)
	turtle.forward(150)

	# position turtle
	turtle.penup()
	turtle.right(180)
	turtle.forward(150)
	turtle.left(90)
	turtle.forward(30)
	turtle.pendown()

	# D
	turtle.circle((150 // 2), 180)
	turtle.left(90)
	turtle.forward(150)

	# position turtle
	turtle.penup()
	turtle.left(90)
	turtle.forward((150 // 2) + 30)
	turtle.pendown()

	# E
	longLine = 100
	shortLine = 60
	turtle.left(90)
	turtle.forward(150)
	turtle.right(90)
	turtle.forward(longLine)
	turtle.penup()
	turtle.right(180)
	turtle.forward(longLine)
	turtle.left(90)
	turtle.forward(150 // 2)
	turtle.left(90)
	turtle.pendown()
	turtle.forward(shortLine)
	turtle.penup()
	turtle.right(180)
	turtle.forward(shortLine)
	turtle.left(90)
	turtle.forward (150 // 2)
	turtle.left(90)
	turtle.pendown()
	turtle.forward(longLine)

	# position turtle
	turtle.penup()
	turtle.forward(30)
	turtle.pendown()
	
	# R
	turtle.left(90)
	turtle.forward(150 // 2)
	turtle.right(90)
	turtle.circle((150 / 4), 180)
	turtle.left(90)
	turtle.forward(150 // 2)
	diagonal = math.sqrt((75**2) + (37.5**2))
	angle = math.degrees(math.asin((150 / 4)/diagonal))
	turtle.left(angle)
	turtle.forward(diagonal)

def clearScreen():
	turtle.clear()
	turtle.reset()

main()
