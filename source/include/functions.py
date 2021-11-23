# TIC TAC TOE by (legal name Ahil, preffered name Bea), 2021
import random


def isWinner(bo,le) -> bool:  # check to see if the board has any lines
    return ((bo[6] == le and bo[7] == le and bo[8] == le) or  # across top
            (bo[3] == le and bo[4] == le and bo[5] == le) or  # across middle
            (bo[0] == le and bo[1] == le and bo[2] == le) or  # across bottom
            (bo[6] == le and bo[3] == le and bo[0] == le) or  # down left
            (bo[7] == le and bo[4] == le and bo[1] == le) or  # down middle
            (bo[8] == le and bo[5] == le and bo[2] == le) or  # down right
            (bo[6] == le and bo[4] == le and bo[2] == le) or  # diagonal
            (bo[8] == le and bo[4] == le and bo[0] == le))  # diagonal


def isMoveAvailable(board,move) -> bool:  # checks if the move can happen
    if (board[move]) is True:  # is there an X in the spot
        return False  # if so, that spot is not available
    if (board[move]) is False:  # is there an O in the spot
        return False  # if so, that spot is not available
    else:
        return True  # this move is available


def boardFull(board):  # are they no more free spaces on the board
    for i in range(1, 10):
        if isMoveAvailable(board, i-1):  # is the spot free?
            return False  # if so, then the board is not full
    return True  # the board is full
