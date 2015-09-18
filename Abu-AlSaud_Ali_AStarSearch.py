#Name: Ali Abu AlSaud
#Date: 9/18/2015
#Assignment 3 A* Search, finding the solution for the maze

#Importing the array library, that is going to be used later
from array import*

#Maze class that will store each maze in a dictionary format
class maze():
	
	#Constructor
	def __init__(Maze):
		Maze.dictionary = {}
	
	#Method to add vertex to the dictionary, in my situation, to add a row number from the maze
	def addVertex(Maze, value):
		newDictionary = {value:[]}
		Maze.dictionary.update(newDictionary)
	
	#Method to add punch of numbers inside the row, which is in my case the numbers in each colomn on that specific row
	def addEdge(Maze, row, element):
		if Maze.dictionary.has_key(row):
			Maze.dictionary.get(row).append(element)
		else:
			print "The row cannot be found."
			
	#Method that will return the content of the position that you entered (row, colomn)
	def location(Maze, row, Position):
		my_array = array('i', [])
		for elements in Maze.dictionary.get(8-row):
			my_array.append(int(format(elements)))
		return my_array[Position-1]

#Function that calculate the Manhattan Distance
def ManhattanDistance(row, colomn):
	return ( (8 - row) + (10 - colomn) ) * 10

#Function that calculate the Euclidean Distance
#Euclidean Distance means the shortest path to the goal, which is calculated by Pythagorean Theorem
def EuclideanDistance(row, colomn):
	rowSquare = (10 - row) ** (2)
	colomnSquare = (10 - colomn) ** (2)
	return ( (rowSquare + colomnSquare) ** (0.5) ) * 12 #12 is an approximate cost (multiple) from each point to the goal

Maze1 = maze()
Maze2 = maze()
#Reading the data from the files to the mazes variables:
with open('World1.txt') as world1:
	for i in range(8):
		Maze1.addVertex(i)
		for j in range(10):
			Maze1.addEdge(i, world1.readline(1))
			world1.readline(1)
with open('World2.txt') as world2:
	for i in range(8):
		Maze2.addVertex(i)
		for j in range(10):
			Maze2.addEdge(i, world2.readline(1))
			world2.readline(1)
			
#The A Star Evaluation Function that uses Manhattan Function
def AstarEvaluationManhattan(currentRow, currentColomn, pathCost, maze, visitedManhattan):
	#If statement to indicate whether we finished or not
	if currentRow == 8 and currentColomn == 10:
		print ("Nodes Evaluated = {}"). format(visitedManhattan)
		return
	else:
		#First, we will calculate the cost of every possible move from the current position:
		
		#This if statement just to make sure that we don't go out of the maze border
		if currentRow + 1 < 9:
			if maze.location(currentRow + 1, currentColomn) == 2:
				costToUp = 999		#I put 999 when the move is to a wall just to say that it is very costly going onto a wall, that we will ignore it
				visitedManhattan = visitedManhattan + 1
			elif maze.location(currentRow + 1, currentColomn) == 1:
				costToUp = 20 + ManhattanDistance(currentRow + 1, currentColomn)
				visitedManhattan = visitedManhattan + 1
			elif maze.location(currentRow + 1, currentColomn) == 0:
				costToUp = 10 + ManhattanDistance(currentRow + 1, currentColomn)
				visitedManhattan = visitedManhattan + 1
		else:
			costToUp = 999
		
		#This if statement just to make sure that we don't go out of the maze border	
		if currentColomn + 1 < 11:
			if maze.location(currentRow, currentColomn + 1) == 2:
				costToRight = 999
				visitedManhattan = visitedManhattan + 1
			elif maze.location(currentRow, currentColomn + 1) == 1:
				costToRight = 20 + ManhattanDistance(currentRow, currentColomn + 1)
				visitedManhattan = visitedManhattan + 1
			elif maze.location(currentRow, currentColomn + 1) == 0:
				costToRight = 10 + ManhattanDistance(currentRow, currentColomn + 1)
				visitedManhattan = visitedManhattan + 1
		else:
			costToRight = 999
		
		#This if statement just to make sure that we don't go out of the maze border	
		if currentRow + 1 < 9 and currentColomn + 1 < 11:
			if maze.location(currentRow + 1, currentColomn + 1) == 2:	
				costToUpRight = 999
				visitedManhattan = visitedManhattan + 1
			elif maze.location(currentRow + 1, currentColomn + 1) == 1:
				costToUpRight = 24 + ManhattanDistance(currentRow + 1, currentColomn + 1)
				visitedManhattan = visitedManhattan + 1
			elif maze.location(currentRow + 1, currentColomn + 1) == 0:
				costToUpRight = 14 + ManhattanDistance(currentRow + 1, currentColomn + 1)
				visitedManhattan = visitedManhattan + 1
		else:
			costToUpRight = 999			
		
		#This if statement just to make sure that we don't go out of the maze border	
		if currentRow + 1 < 9 and currentColomn - 1 < 11 and currentColomn - 1 > 0:
			if maze.location(currentRow + 1, currentColomn - 1) == 2:	
				costToUpLeft = 999
				visitedManhattan = visitedManhattan + 1
			elif maze.location(currentRow + 1, currentColomn - 1) == 1:
				costToUpLeft = 24 + ManhattanDistance(currentRow + 1, currentColomn - 1)
				visitedManhattan = visitedManhattan + 1
			elif maze.location(currentRow + 1, currentColomn - 1) == 0:
				costToUpLeft = 14 + ManhattanDistance(currentRow + 1, currentColomn - 1)
				visitedManhattan = visitedManhattan + 1
		else:
			costToUpLeft = 999
		
		#This if statement just to make sure that we don't go out of the maze border	
		if currentRow - 1 < 9 and currentRow - 1 > 0 and currentColomn + 1 < 11:
			if maze.location(currentRow - 1, currentColomn + 1) == 2:	
				costToDownRight = 999
				visitedManhattan = visitedManhattan + 1
			elif maze.location(currentRow - 1, currentColomn + 1) == 1:
				costToDownRight = 24 + ManhattanDistance(currentRow - 1, currentColomn + 1)
				visitedManhattan = visitedManhattan + 1
			elif maze.location(currentRow - 1, currentColomn + 1) == 0:
				costToDownRight = 14 + ManhattanDistance(currentRow - 1, currentColomn + 1)
				visitedManhattan = visitedManhattan + 1
		else:
			costToDownRight = 999
			
		#Now we will figure out the cheapest cost of every move:
		if costToUp <= costToRight and costToUp <= costToUpRight and costToUp <= costToUpLeft and costToUp <= costToDownRight:
			currentRow = currentRow + 1
			pathCost = pathCost + costToUp - ManhattanDistance(currentRow, currentColomn)
			print("Move to ({}, {})"). format(currentRow, currentColomn)
			print("Path Cost = {}"). format(pathCost)
			AstarEvaluationManhattan(currentRow, currentColomn, pathCost, maze, visitedManhattan)
		elif costToRight <= costToUp and costToRight <= costToUpRight and costToRight <= costToUpLeft and costToRight <= costToDownRight:
			currentColomn = currentColomn + 1
			pathCost = pathCost + costToRight - ManhattanDistance(currentRow, currentColomn)
			print("Move to ({}, {})"). format(currentRow, currentColomn)
			print("Path Cost = {}"). format(pathCost)
			AstarEvaluationManhattan(currentRow, currentColomn, pathCost, maze, visitedManhattan)
		elif costToUpRight <= costToRight and costToUpRight <= costToUp and costToUpRight <= costToUpLeft and costToUpRight <= costToDownRight:
			currentRow = currentRow + 1
			currentColomn = currentColomn + 1
			pathCost = pathCost + costToUpRight - ManhattanDistance(currentRow, currentColomn)
			print("Move to ({}, {})"). format(currentRow, currentColomn)
			print("Path Cost = {}"). format(pathCost)
			AstarEvaluationManhattan(currentRow, currentColomn, pathCost, maze, visitedManhattan)
		elif costToUpLeft <= costToRight and costToUpLeft <= costToUp and costToUpLeft <= costToUpRight and costToUpLeft <= costToDownRight:
			currentRow = currentRow + 1
			currentColomn = currentColomn - 1
			pathCost = pathCost + costToUpLeft - ManhattanDistance(currentRow, currentColomn)
			print("Move to ({}, {})"). format(currentRow, currentColomn)
			print("Path Cost = {}"). format(pathCost)
			AstarEvaluationManhattan(currentRow, currentColomn, pathCost, maze, visitedManhattan)
		elif costToDownRight <= costToRight and costToDownRight <= costToUp and costToDownRight <= costToUpRight and costToDownRight <= costToUpLeft:
			currentRow = currentRow - 1
			currentColomn = currentColomn + 1
			pathCost = pathCost + costToDownRight - ManhattanDistance(currentRow, currentColomn)
			print("Move to ({}, {})"). format(currentRow, currentColomn)
			print("Path Cost = {}"). format(pathCost)
			AstarEvaluationManhattan(currentRow, currentColomn, pathCost, maze, visitedManhattan)

#The A Star Evaluation Function that uses Euclidean Function
def AstarEvaluationEuclidean(currentRow, currentColomn, pathCost, maze, visitedEuclidean):
	#If statement to indicate whether we finished or not
	if currentRow == 8 and currentColomn == 10:
		print("Nodes Evaluated = {}"). format(visitedEuclidean)
		return
	else:
		#First, we will calculate the cost of every possible move from the current position:
		
		#This if statement just to make sure that we don't go out of the maze border
		if currentRow + 1 < 9:
			if maze.location(currentRow + 1, currentColomn) == 2:
				costToUp = 999		#I put 999 when the move is to a wall just to say that it is very costly going onto a wall, that we will ignore it
				visitedEuclidean = visitedEuclidean + 1
			elif maze.location(currentRow + 1, currentColomn) == 1:
				costToUp = 20 + EuclideanDistance(currentRow + 1, currentColomn)
				visitedEuclidean = visitedEuclidean + 1
			elif maze.location(currentRow + 1, currentColomn) == 0:
				costToUp = 10 + EuclideanDistance(currentRow + 1, currentColomn)
				visitedEuclidean = visitedEuclidean + 1
		else:
			costToUp = 999
		
		#This if statement just to make sure that we don't go out of the maze border	
		if currentColomn + 1 < 11:
			if maze.location(currentRow, currentColomn + 1) == 2:
				costToRight = 999
				visitedEuclidean = visitedEuclidean + 1
			elif maze.location(currentRow, currentColomn + 1) == 1:
				costToRight = 20 + EuclideanDistance(currentRow, currentColomn + 1)
				visitedEuclidean = visitedEuclidean + 1
			elif maze.location(currentRow, currentColomn + 1) == 0:
				costToRight = 10 + EuclideanDistance(currentRow, currentColomn + 1)
				visitedEuclidean = visitedEuclidean + 1
		else:
			costToRight = 999
		
		#This if statement just to make sure that we don't go out of the maze border	
		if currentRow + 1 < 9 and currentColomn + 1 < 11:
			if maze.location(currentRow + 1, currentColomn + 1) == 2:	
				costToUpRight = 999
				visitedEuclidean = visitedEuclidean + 1
			elif maze.location(currentRow + 1, currentColomn + 1) == 1:
				costToUpRight = 24 + EuclideanDistance(currentRow + 1, currentColomn + 1)
				visitedEuclidean = visitedEuclidean + 1
			elif maze.location(currentRow + 1, currentColomn + 1) == 0:
				costToUpRight = 14 + EuclideanDistance(currentRow + 1, currentColomn + 1)
				visitedEuclidean = visitedEuclidean + 1
		else:
			costToUpRight = 999			
		
		#This if statement just to make sure that we don't go out of the maze border	
		if currentRow + 1 < 9 and currentColomn - 1 < 11 and currentColomn - 1 > 0:
			if maze.location(currentRow + 1, currentColomn - 1) == 2:	
				costToUpLeft = 999
				visitedEuclidean = visitedEuclidean + 1
			elif maze.location(currentRow + 1, currentColomn - 1) == 1:
				costToUpLeft = 24 + EuclideanDistance(currentRow + 1, currentColomn - 1)
				visitedEuclidean = visitedEuclidean + 1
			elif maze.location(currentRow + 1, currentColomn - 1) == 0:
				costToUpLeft = 14 + EuclideanDistance(currentRow + 1, currentColomn - 1)
				visitedEuclidean = visitedEuclidean + 1
		else:
			costToUpLeft = 999

		#This if statement just to make sure that we don't go out of the maze border	
		if currentRow - 1 < 9 and currentColomn + 1 < 11 and currentRow - 1 > 0:
			if maze.location(currentRow - 1, currentColomn + 1) == 2:	
				costToDownRight = 999
				visitedEuclidean = visitedEuclidean + 1
			elif maze.location(currentRow - 1, currentColomn + 1) == 1:
				costToDownRight = 24 + EuclideanDistance(currentRow - 1, currentColomn + 1)
				visitedEuclidean = visitedEuclidean + 1
			elif maze.location(currentRow - 1, currentColomn + 1) == 0:
				costToDownRight = 14 + EuclideanDistance(currentRow - 1, currentColomn + 1)
				visitedEuclidean = visitedEuclidean + 1
		else:
			costToDownRight = 999
		
		print("Cost to Up: {}"). format(costToUp)
		print("Cost to Right: {}"). format(costToRight)
		print("Cost to UpRight: {}"). format(costToUpRight)
		print("Cost to UpLeft: {}"). format(costToUpLeft)
		print("Cost to DownRight: {}"). format(costToDownRight)
		
	
		#Now we will figure out the cheapest cost of every move:
		if costToUp <= costToRight and costToUp <= costToUpRight and costToUp <= costToUpLeft and costToUp <= costToDownRight:
			currentRow = currentRow + 1
			pathCost = pathCost + costToUp - EuclideanDistance(currentRow, currentColomn)
			print("Move to ({}, {})"). format(currentRow, currentColomn)
			print("Path Cost = {}"). format(pathCost)
			AstarEvaluationEuclidean(currentRow, currentColomn, pathCost, maze, visitedEuclidean)
		elif costToRight <= costToUp and costToRight <= costToUpRight and costToRight <= costToUpLeft and costToRight <= costToDownRight:
			currentColomn = currentColomn + 1
			pathCost = pathCost + costToRight - EuclideanDistance(currentRow, currentColomn)
			print("Move to ({}, {})"). format(currentRow, currentColomn)
			print("Path Cost = {}"). format(pathCost)
			AstarEvaluationEuclidean(currentRow, currentColomn, pathCost, maze, visitedEuclidean)
		elif costToUpRight <= costToRight and costToUpRight <= costToUp and costToUpRight <= costToUpLeft and costToUpRight <= costToDownRight:
			currentRow = currentRow + 1
			currentColomn = currentColomn + 1
			pathCost = pathCost + costToUpRight - EuclideanDistance(currentRow, currentColomn)
			print("Move to ({}, {})"). format(currentRow, currentColomn)
			print("Path Cost = {}"). format(pathCost)
			AstarEvaluationEuclidean(currentRow, currentColomn, pathCost, maze, visitedEuclidean)
		elif costToUpLeft <= costToRight and costToUpLeft <= costToUp and costToUpLeft <= costToUpRight and costToUpLeft <= costToDownRight:
			currentRow = currentRow + 1
			currentColomn = currentColomn - 1
			pathCost = pathCost + costToUpLeft - EuclideanDistance(currentRow, currentColomn)
			print("Move to ({}, {})"). format(currentRow, currentColomn)
			print("Path Cost = {}"). format(pathCost)
			AstarEvaluationEuclidean(currentRow, currentColomn, pathCost, maze, visitedEuclidean)
		elif costToDownRight <= costToRight and costToDownRight <= costToUp and costToDownRight <= costToUpRight and costToDownRight <= costToUpLeft:
			currentRow = currentRow - 1
			currentColomn = currentColomn + 1
			pathCost = pathCost + costToDownRight - EuclideanDistance(currentRow, currentColomn)
			print("Move to ({}, {})"). format(currentRow, currentColomn)
			print("Path Cost = {}"). format(pathCost)
			AstarEvaluationEuclidean(currentRow, currentColomn, pathCost, maze, visitedEuclidean)


currentRow = 1
currentColomn = 1
pathCost = 0
visitedManhattan = 0
visitedEuclidean = 0

#The testing part of the code		
mazeNumber = input("Enter the number of maze that you want to solve: ")
HFunction = input("Enter 1 to choose the Manhattan Distance \nEnter 2 to choose the Euclidean Distance \n")
if mazeNumber == 1:
	if HFunction == 1:
		AstarEvaluationManhattan(currentRow, currentColomn, pathCost, Maze1, visitedManhattan)
	elif HFunction == 2:
		AstarEvaluationEuclidean(currentRow, currentColomn, pathCost, Maze1, visitedEuclidean)
	else:
		print("Sorry the number that you entered is out of range")
elif mazeNumber == 2:
	if HFunction == 1:
		AstarEvaluationManhattan(currentRow, currentColomn, pathCost, Maze2, visitedManhattan)
	elif HFunction == 2:
		AstarEvaluationManhattan(currentRow, currentColomn, pathCost, Maze2, visitedEuclidean)
	else:
		print("Sorry the number that you entered is out of range")
else:
	print("Sorry the number that you entered is out of range")
