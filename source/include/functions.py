import random
# from include import const

def startingPlayer() -> bool:
    if random.randint(0,1) == 0:
        return True
    else:
        return False

def getBoardCopy(board):
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

def isWinner(bo,le) -> bool:
    return ((bo[6] == le and bo[7] == le and bo[8] == le) or # across the top
    (bo[3] == le and bo[4] == le and bo[5] == le) or # across the middle
    (bo[0] == le and bo[1] == le and bo[2] == le) or # across the bottom
    (bo[6] == le and bo[3] == le and bo[0] == le) or # down the left side
    (bo[7] == le and bo[4] == le and bo[1] == le) or # down the middle
    (bo[8] == le and bo[5] == le and bo[2] == le) or # down the right side
    (bo[6] == le and bo[4] == le and bo[2] == le) or # diagonal
    (bo[8] == le and bo[4] == le and bo[0] == le)) # diagonal

def isMoveAvailable(board,move) -> bool:
    if (board[move]) == True:
        return False
    if (board[move]) == False:
        return False
    else:
        return True

def getRandom(board,moves) -> int:
    possible_moves = []
    for i in moves:
        if isMoveAvailable(board,i):
            possible_moves.append(i)
    if len(possible_moves) != 0:
        return random.choice(possible_moves)
    else:
        return None

def makeMove(board, letter, move ):
    if isMoveAvailable(board, move):
        board[move] = letter

def getImpossibleMove(board, comp_letter, player_first, turn):
    if comp_letter:
        player_letter = False
    else:
        player_letter = True
    # Check for each place in the board

    for i in range(0, 9):
        copy = getBoardCopy(board)
        makeMove(copy, comp_letter, i)
        if isWinner(copy, comp_letter):
            return i

    # Check if player could win in next move, and block them
    for i in range(0, 9):
        copy = getBoardCopy(board)
        makeMove(copy, player_letter, i)
        if isWinner(copy, player_letter):
            return i

    if player_first == True:
        if isMoveAvailable(board, 4):
            return 4

    if turnNumber == 2 and player_first == True:
        move = getRandom(board, [1, 3, 5, 7])
        if move != None:
            return move

    # Take one of the cornors is free, using the Choose random move from list function
    move = getRandom(board, [6, 8, 0, 2])
    if move != None:
        return move
    # Try to take the center if free
    if isMoveAvailable(board, 4):
        return 4

    # Take on of the sides. Using the choose random move from list function
    move = getRandom(board, [1,3,5,7])
    if move != None:
        return move

def getBeginnerMove(board, computerletter):
    move = getRandom(board, [0,1,2,3,4,5,6,7,8])
    if move != None:
        return move

def getEasyMove(board, computerletter):
    if computerletter == 'X':
        playersLetter = 'O'
    else:
        playersLetter = 'X'

    for i in range(1, 10):
        copy = getBoardCopy(board)
        makeMove(copy, computerletter, i-1)
        if isWinner(copy, computerletter):
            return i-1
    # Check if player could win in next move, and block them
    for i in range(1, 10):
        copy = getBoardCopy(board)
        makeMove(copy, playersLetter, i-1)
        if isWinner(copy, playersLetter):
            return i-1

    move = getRandom(board, [0,1,2,3,4,5,6,7,8])
    if move != None:
        return move

def getHardMove(board, computerletter):
    if computerletter:
        playersLetter = False
    else:
        playersLetter = True

    for i in range(1, 10):
        copy = getBoardCopy(board)
        makeMove(copy, computerletter, i-1)
        if isWinner(copy, computerletter):
            return i-1
    # Check if player could win in next move, and block them
    for i in range(1, 10):
        copy = getBoardCopy(board)
        makeMove(copy, playersLetter, i-1)
        if isWinner(copy, playersLetter):
            return i-1

    move = getRandom(board, [6, 8, 0, 2])
    if move != None:
        return move
    # Try to take the center if free
    if isMoveAvailable(board, 4):
        return 4

    move = getRandom(board, [1,3,5,7])
    if move != None:
        return move

def getCompMove(board, computerletter, player_first, turnNumber, difficulty):
    if difficulty == 0:
        move = getBeginnerMove(board, computerletter)
        return move
    if difficulty == 1:
        move = getEasyMove(board, computerletter)
        return move
    if difficulty == 2:
        move = getHardMove(board, computerletter)
        return move
    if difficulty == 3:
        move = getImpossibleMove(board, computerletter, player_first, turnNumber)
        return move

def boardFull(board):
    for i in range(1, 10):
        if isMoveAvailable(board, i-1):
            return False
    return True