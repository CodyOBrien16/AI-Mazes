import random
#create the 8x8 maze
maze = [
    [1, 1, 0, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 1],
    [1, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 1],
    [1, 1, 0, 0, 0, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 0, 1],
]

# solution improvement ideas
# if there are only one possible visited cell then go there and replace previous cell with wall
# if there are two possible visited cells then pick one but dont replace previous cell with wall

visitedCells = []
startx = 0
starty = 2
endX = 7
endY = 6
currentPosX = startx
currentPosY = starty
totalSteps = 0

while (True):
    #do algorithm
    if currentPosX == endX and currentPosY == endY:
        break

    possibleMoves = []
    possibleVisitedMoves = []
    visitedCells.append([currentPosX, currentPosY])

    for row in maze:
        print(row)
    print("Current Position: ", currentPosX, currentPosY)
    
    #need to to add if visited
    #look down
    if maze[currentPosX + 1][currentPosY] == 0 and [currentPosX + 1, currentPosY] not in visitedCells:
        possibleMoves.append("down")
    
    #look right
    if maze[currentPosX][currentPosY + 1] == 0 and [currentPosX, currentPosY + 1] not in visitedCells:
        possibleMoves.append("right")

    #look left
    if maze[currentPosX][currentPosY - 1] == 0 and [currentPosX, currentPosY - 1] not in visitedCells:
        possibleMoves.append("left")

    #look up
    if maze[currentPosX - 1][currentPosY] == 0 and [currentPosX - 1, currentPosY] not in visitedCells:
        possibleMoves.append("up")

    if len(possibleMoves) == 0:
        if maze[currentPosX + 1][currentPosY] == 0:
            possibleVisitedMoves.append("down")
        if maze[currentPosX][currentPosY + 1] == 0:
            possibleVisitedMoves.append("right")
        if maze[currentPosX][currentPosY - 1] == 0:
            possibleVisitedMoves.append("left")
        if maze[currentPosX - 1][currentPosY] == 0:
            possibleVisitedMoves.append("up")
        if len(possibleVisitedMoves) == 0:
            break
        move = random.randint(0, len(possibleVisitedMoves) -1)
        if possibleVisitedMoves[move] == "down":
            currentPosX += 1
        elif possibleVisitedMoves[move] == "right":
            currentPosY += 1
        elif possibleVisitedMoves[move] == "left":
            currentPosY -= 1
        elif possibleVisitedMoves[move] == "up":
            currentPosX -= 1

    else:
        move = random.randint(0, len(possibleMoves) -1)
        if possibleMoves[move] == "down":
            currentPosX += 1
        elif possibleMoves[move] == "right":
            currentPosY += 1
        elif possibleMoves[move] == "left":
            currentPosY -= 1
        elif possibleMoves[move] == "up":
            currentPosX -= 1

    totalSteps += 1

print("Total Steps: ", totalSteps)
print("Visited Cells: ", visitedCells)
print("End Position: ", currentPosX, currentPosY)

    

