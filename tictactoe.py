board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

def gameLoop():
    currentPlayer = 1
    players = ['X', 'O']

    while(not gameOver()):
        position = getPlayerInput(currentPlayer)
        updateBoard(position, players[currentPlayer-1])
        drawBoard()

        if hasWinner():
            print(f'Player {currentPlayer} won!')

        if isBoardFull():
            print('Tie!')
        
        currentPlayer = changePlayer(currentPlayer)

def gameOver():
    return hasWinner() or isBoardFull()

def hasWinner():
    if testLine([0, 1, 2]) or testLine([3, 4, 5]) or testLine([6, 7, 8]) or testLine([0, 3, 6]) or testLine([1, 4, 7]) or testLine([2, 5, 8]) or testLine([0, 4, 8]) or testLine([2, 4, 6]):
        return True
    return False

def testLine(positions):
    if ' ' in [board[positions[0]], board[positions[1]], board[positions[2]]]:
        return False
    if board[positions[0]] == board[positions[1]] == board[positions[2]]:
        return True
    return False

def isBoardFull():
    return ' ' not in board

def getPlayerInput(player):

    position = int(input(f'Enter a position player {player}: '))
    while(not isPositionValid(position)):
        print('Invalid position!')
        position = int(input(f'Enter a valid position player {player}: '))

    return position

def isPositionValid(position):
    return board[position] == ' '

def changePlayer(player):
    return 2 if player == 1 else 1

def updateBoard(position, player):
    board[position] = player

def drawBoard():
    print(f'{board[0]}|{board[1]}|{board[2]}')
    print('-+-+-')
    print(f'{board[3]}|{board[4]}|{board[5]}')
    print('-+-+-')
    print(f'{board[6]}|{board[7]}|{board[8]}')

gameLoop()