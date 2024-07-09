import random

print("----------------------------")
# Print a separator line
possibleNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

gameBoard = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Initialize the game board in a matrix
rows = 3
columns = 3

# Function to print the game board it'll be a matrix for tic tac toe
def printGameBoard():
    for x in range(rows):
        print("\n+----+----+----+")
        print("|", end="")
        for y in range(columns):
            print(" ", gameBoard[x][y], end=" |")
    print("\n+----+----+----+")
# Function to modify the game board based on user input
def modifyArray(num, turn):
    num -= 1
    gameBoard[num // 3][num % 3] = turn

def checkForWinner(board):
    # Check rows and columns for victory (rules fro winning)
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]
    # Check diagonals for victory
    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    # when no winners found
    return None

def isBoardFull(board):
    return all(isinstance(cell, str) for row in board for cell in row)

leaveLoop = False
turnCounter = 0
# main game
while not leaveLoop:
    printGameBoard()
    if turnCounter % 2 == 0:
#players turn to choose an number to mark in order to win
        numberPicked = int(input("\nChoose a number [1-9]: "))
        if numberPicked in possibleNumbers:
            modifyArray(numberPicked, 'X')
            possibleNumbers.remove(numberPicked)
            turnCounter += 1
        else:
            print("Invalid input or cell already taken. Please try again.")
    else:
        cpuChoice = random.choice(possibleNumbers)
        print("\nCpu choice:", cpuChoice)
        modifyArray(cpuChoice, 'O')
        possibleNumbers.remove(cpuChoice)
        turnCounter += 1
    
    winner = checkForWinner(gameBoard)
    if winner:
        printGameBoard()
        print(f"\n{winner} has won!")
        leaveLoop = True
# to check if it's a draw
    elif isBoardFull(gameBoard):
        printGameBoard()
        print("\nIt's a draw!")
        leaveLoop = True

print("\nGame over! Thank you for playing :)")
