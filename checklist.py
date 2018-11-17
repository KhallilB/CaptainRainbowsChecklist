import os

checklist = list()

def create(item):
	checklist.append(item)

def read(index):
	item = checklist[int(index)]
	return item

def update(index, item):
	checklist[index] = item

def destroy(index): 
	checklist.pop(index)

def listAllItems():
	index = 0
	for listItem in checklist:
		print("{} {}".format(index, listItem))
		index += 1

def markCompleted(index):
	checklist[index] = "√" + checklist[index]
	
def select(functionCode):
	#Create item
	if functionCode == "C":
		inputItem = userInput("Add")
		create(inputItem)

        #Read Item
	elif functionCode == "R":
		itemIndex = userInput("Index Number?")

		print(read(int(itemIndex)))

        #Update Item
	elif functionCode == "U":
		itemUp = userInput("Index?")
		inputUp = userInput("Input item:")
		update(int(itemUp), inputUp)

        #Destroy Item
	elif functionCode == "D":
		itemDel = userInput("Enter Index Number: ")
		destroy(int(itemDel))

	elif functionCode == "M":
		inputMark = userInput("Index Number:")
		markCompleted(int(inputMark))

	elif functionCode == "P":
		listAllItems()

	elif functionCode == "Q":
		return False
	else:
		print("Unknown Option")
	return True

def userInput(prompt):
	# the input function will display a message in the terminal 
	# and wait for user input.
	userInput = input(prompt)
	os.system("clear")
	return userInput


running = True

while running:
	selection = userInput( 
		"Press C to add to list, R to Read from list, U to update list, D to destroy item in list, M to mark list item done, P to display list, and Q to quit:  ")
	running = select(selection)

	
