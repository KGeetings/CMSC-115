import random

def isBoardFull(b):
    for r in range(len(b)):
        for c in range(len(b)):
            if b[r][c] == " ":
                return False
    return True

def playerHasWonRow(board, player, row):
    for i in range(len(board)):
        if board[row][i] != player:
            return False
    return True
    
def playerHasWonCol(board, player, col):
    for i in range(len(board)):
        if board[i][col] != player:
            return False
    return True

def playerHasWonDownDiag(board, player):
    for i in range(len(board)):
        if board[i][i] != player:
            return False
    return True

def playerHasWonUpDiag(board, player):
    for i in range(len(board)):
        if board[len(board)-1-i][i] != player:
            return False
    return True

def gameWon(board , player):
    #Check if player has won by rows
    for row in range(len(board)):
        if playerHasWonRow(board, player, row):
            return True
    #Check if player has won by columns
    for col in range(len(board)):
        if playerHasWonCol(board, player, col):
            return True
    #Check if player has won by down diagonal
    if playerHasWonDownDiag(board, player):
        return True
    #Check if player has won by up diagonal
    if playerHasWonUpDiag(board, player):
        return True
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
    for row in range(len(b)):
        for col in range(len(b)):
            print(" " + b[row][col], end= " ")
            if col < len(b)-1:
                print("|", end = "")
        print()
        if row < len(b) - 1:
            for col in range(len(b)):
                print("---", end= "")
                if col < len(b) -1:
                    print("+", end="")
        print()
        
def getPlayerMove(b):
    printBoard(b)
    row = int(input("Which row would you like to play? ")) - 1
    col = int(input("Which column would you like to play? ")) - 1
    
    while b[row][col] != " ":
        print("No, that spot is already taken.")
        row = int(input("Which row would you like to play? ")) - 1
        col = int(input("Which column would you like to play? ")) - 1
        
    b[row][col] = "X"
    
    printBoard(b)

def getComputerMove(b):
    while True:
        row = random.randrange(len(b))
        col = random.randrange(len(b))
        if b[row][col] == " ":
            break
        
        b[row][col] = "O"
        print(f"The computer picks row {row+1}, column {col+1}.")

boardSize = int(input("how big of a board do you want to play?"))
board = []
for row in range(boardSize):
    board.append([])
    for col in range(boardSize):
        board[row].append(" ")
        

playersTurn = True

while not gameOver(board):
    if playersTurn:
        getPlayerMove(board)
    else:
        getComputerMove(board)
    playersTurn = not playersTurn
    
print("------------------------")
printBoard(board)

if gameWon(board, "X"):
    print("You beat the computer")
elif gameWon(board, "O"):
    print("You lost against the computer")
else:
    print("Cat's game")