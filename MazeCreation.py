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



visitedCells = []
startx = 0
starty = 2
endX = 7
endY = 6
currentPosX = startx
currentPosY = starty
totalSteps = 0

while (currentPosX != endX and currentPosY != endY):
    #do algorithm
    possibleMoves = []
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
        print("No possible moves")
        break
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
    

