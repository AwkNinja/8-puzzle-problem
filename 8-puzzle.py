# 8 puzzle problem using best first Search algorithm

from copy import deepcopy   # for making a copy of a list without reference


checkBoard = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]      # Goal state
memory = []     # used as the priority queue
visited = []    # used to check if a state was already traversed

# for taking the input state of the board
def inputBoard():
    print("Enter the start sate of the board, one number at a time and press enter after each input: ")
    rows, cols = (3, 3)
    arr=[]
    for i in range(rows):
        col = []
        for j in range(cols):
            col.append(int(input()))
        arr.append(col)
    return arr

# function for calculating heuristic
def calcHeuristic(inputBoard, h = 0):
    for i in range(3):
        for j in range(3):
            if checkBoard[i][j] != inputBoard[i][j]:
                h = h + 1
    return h

# function to perform the best first search algo on the board
def move(gameBoard):

    h = calcHeuristic(gameBoard)
    memory.append((h, gameBoard))

    while(len(memory) != 0):

        newGameBoard = deepcopy(gameBoard)

        if checkBoard == newGameBoard:
            return "Goal State Found"

        if gameBoard not in visited:    # check if the path was already traversed

            visited.append(gameBoard)

            # for printing the path taken by the whole algo to get to the result
            for x in gameBoard:
                for i in x:
                    print(i, end = " ")
                print()  

            print("\n  |")
            print("  |")
            print(" \\\'/ \n")

            for j, x in enumerate(gameBoard):
                if 0 in x:
                    row, col = (j, x.index(0))

            if row != 0:
                #move up
                temp = newGameBoard[row][col]
                newGameBoard[row][col] = newGameBoard[row - 1][col]
                newGameBoard[row - 1][col] = temp
                if newGameBoard not in visited:
                    memory.append((calcHeuristic(newGameBoard), newGameBoard))

            newGameBoard = deepcopy(gameBoard)
            if row != 2:
                #move down
                temp = newGameBoard[row][col]
                newGameBoard[row][col] = newGameBoard[row + 1][col]
                newGameBoard[row + 1][col] = temp
                if newGameBoard not in visited:
                    memory.append((calcHeuristic(newGameBoard), newGameBoard))

            newGameBoard = deepcopy(gameBoard)
            if col != 0:
                # move left
                temp = newGameBoard[row][col]
                newGameBoard[row][col] = newGameBoard[row][col - 1]
                newGameBoard[row][col - 1] = temp
                if newGameBoard not in visited:
                    memory.append((calcHeuristic(newGameBoard), newGameBoard))
            
            newGameBoard = deepcopy(gameBoard)
            if col != 2:
                # move right
                temp = newGameBoard[row][col]
                newGameBoard[row][col] = newGameBoard[row][col + 1]
                newGameBoard[row][col + 1] = temp
                if newGameBoard not in visited:
                    memory.append((calcHeuristic(newGameBoard), newGameBoard))


        memory.sort(reverse=True)
        gameBoard = memory.pop()[1]     # returns a tuple so we take the value at the second index so we get the array at the first index is the priority


gameBoard = inputBoard()
print(move(gameBoard))
