#TIC-TAC-TOE

import random

def drawBoard(board): #Prints and Makes the board 

    print(board[7]+ '|' + board[8]+ '|'+ board[9])
    print('-+-+-')
    print(board[4]+ '|' + board[5]+ '|' +board[6])
    print('-+-+-')
    print(board[1]+ '|' + board[2]+ '|' +board[3])

def inputPlayerLetter(): #gets the letter that the player wants 
    letter=''
    while not (letter=='X' or letter =='O'):
        print('Do you want to be X or O')
        letter=input().upper()

    if letter=='X':
        return ['X' , 'O']
               
    else:
        return['O', 'X']

def whoGoesFirst(): #Picks who goes first 
    if random.randint(0,1)==0:
        return 'computer'
    else:
        return 'player'

def makeMove(board, letter, move): #adds moves to the board
    board[move] = letter

def isWinner(bo, le): #checks to see if there is a winner
               
    return ((bo[7]==le and bo[8]==le and bo[9]==le) or
            (bo[4]==le and bo[5]==le and bo[6]==le) or
            (bo[1]==le and bo[2]==le and bo[3]==le) or
            (bo[7]==le and bo[4]==le and bo[1]==le) or
            (bo[8]==le and bo[5]==le and bo[2]==le) or
            (bo[9]==le and bo[6]==le and bo[3]==le) or
            (bo[7]==le and bo[5]==le and bo[3]==le) or
            (bo[9]==le and bo[5]==le and bo[1]==le))

def getBoardCopy(board): #copies the board
    boardCopy= [ ]
    for i in board:
        boardCopy.append(i)
    return boardCopy

def isSpaceFree(board, move): #checks to find a free space 
    return board[move] == ' '

def getPlayerMove(board): # gets the players move 
    move=' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)')
        move=input()
               
    return int(move)

def chooseRandomMoveFromList(board, movesList):
    possibleMove=[]
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMove.append(i)
               
    if len(possibleMove)!= 0:
        return random.choice(possibleMove)
    else:
        return None

def getComputerMove(board, computerLetter): #gets the computers move 

    if computerLetter=='X':
        playerLetter=='O'
    else:
        playerLetter=='X'

    for i in range(1,10): #finds a winning move
        boardCopy=getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, computerLetter, i)
            if isWinner(boardCopy, computerLetter):
               return i
               
    for i in range (1, 10): #blocks player from winning
        boardCopy=getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, playerLetter, i)
            if isWinner(boardCopy, playerLetter):
               return i

    move = chooseRandomMoveFromList(board,[7,9,1,3]) #takes a conner spot

    if move != None:
        return move

    if isSpaceFree(board, 5): #Takes the center spot
        return 5

    return chooseRandomMove(board,[2,4,6,8])

def isBoardFull(board):
    
     for i in range(1,10):
        if isSpaceFree(board, i):
            return False
               
     return True

print('Welcome to TIC-TAC-TOE')

while True:
    theBoard=[' ']*10
    playerLetter, computerLetter= inputPlayerLetter()
    turn = whoGoesFirst()
    print('The '+ turn + ' will go first')
    gameIsPlaying=True

    while gameIsPlaying:
        if turn== 'player':
            drawBoard(theBoard)
            move=getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('The player won')
                gameIsPlaying = False

            else:
               if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('This was a tie')
                    break
               else:
                   turn='computer'
        else:
            move=getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
               drawBoard(theBoard)
               print('The computer won')
               gameIsPlaying = False

            else:
               if isBoardFull(theBoard):
                   drawBoard(theBoard)
                   print('This was a tie')
                   break
               else:
                   turn='player'
    print('Do you want to play again? (yes or no')
    if not input().lower().startswith('y'):
        break
        
        

























