import random

def isBoardFull(b):
    for r in range(3):
        for c in range(3):
            if b[r][c] == " ":
                return False
    return True

def gameWon(board , player):
    #Check if player has won by rows
    for row in range(3):
        if playerHasWonRow(board, player, row):
            return True
    #Check if player has won by columns
    for col in range(3):
        if playerHasWonColumn(board, player, col):
            return True
    #Check if player has won by down diagonal
    #Check if player has won by up diagonal
    
    #IF I get here they must not have won
    return False

def gameOver(b):
    if gameWon(b, "X"):
        return True
    if gameWon(b, "O"):
        return True
    if isBoardFull(b):
        return True
    
    return False

def printBoard(b):
    for row in range(3):
        for col in range(3):
            print(" " + b[row][col], end= " ")
            if col < 2:
                print("|", end = "")
        print()
        if row < 2:
            print("---+---+---")
        
def getPlayerMove(b):
    printBoard(b)
    row = int(input("Which row would you like to play? ")) - 1
    col = int(input("Which column would you like to play? ")) - 1
    
    b[row][col] = "X"
    
    printBoard(b)

def getComputerMove(b):
    amIDone = False
    while not amIDone:
        row = random.randrange(3)
        col = random.randrange(3)
        if b[row][col] == " ":
            amIDone = True
        
        b[row][col] = "O"
        print(f"The computer picks row {row+1}, column {col+1}.")


board = [ [" ", " ", " "], [" ", " ", " "], [" ", " ", " "] ]

playersTurn = True

while not gameOver(board):
    if playersTurn:
        getPlayerMove(board)
    else:
        getComputerMove(board)
    playersTurn = not playersTurn