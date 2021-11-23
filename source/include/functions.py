import random
# from include import const


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

def boardFull(board):
    for i in range(1, 10):
        if isMoveAvailable(board, i-1):
            return False
    return True