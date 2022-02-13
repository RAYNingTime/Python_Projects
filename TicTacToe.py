import random

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
currentPlayer = "X"
winner = None
gameRunning = True

# printing the game board

def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print("")

# take player input

def playerInput(board):
    print("Now is your turn! Select your position!")
    inp = int(input("Enter a number 1-9: "))
    if inp >= 1 and inp <= 9 and board[inp-1] == "-":
        board[inp-1] = currentPlayer
    else: print("Oops. Probably this spot already taken or doesn't exist.")

# check for win or tie
def checkHorizontle(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True

def checkDiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True

def checkTie(board):
    global gameRunning
    if "-" not in board and (checkDiag(board) == checkHorizontle(board) == checkRow(board) == False):
        printBoard(board)
        print("It's a tie!")
        gameRunning = False

def checkWin(board):
    global  gameRunning
    if checkDiag(board) or checkHorizontle(board) or checkRow(board):
        print("")
        print(f"The winner is {winner}")
        print("")
        gameRunning = False
# switch the player

def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

# computer

def computer(board):
    print("Now your opponent turn! Wait for his choice!")
    while currentPlayer == "O":
        position = random.randint(0,8)
        if board[position] == "-":
            board[position] = "0"
            switchPlayer()
# check for win or tie again

while gameRunning:
    printBoard(board)
    playerInput(board)
    switchPlayer()
    checkWin(board)
    checkTie(board)
    if gameRunning:
        computer(board)
        checkWin(board)
        checkTie(board)
    if winner != None:
        printBoard(board)