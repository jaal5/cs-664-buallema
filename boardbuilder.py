from constraint import *
from brute import *

from random import sample

def remove(brd, difficulty = 10):
    while True:
        #print(rem)
        r = sample(range(9),1)[0]
        c = sample(range(9),1)[0]
        backup  = brd[r][c]
        brd[r][c] = 0
        board = copy.deepcopy(brd)
        s = solve_difficulty(board, difficulty)
        if not s:
            brd[r][c] = backup
            return brd
            break

def possiblevalues(board, pos):
    possiblevalues = []
    for val in range (1,10):
        if constraintsatisfaction(board, val, pos):
            #print(constraintsatisfaction(board, i, emptycell))
            possiblevalues.append(val)
    return possiblevalues

def build_board(prefill=5):

    board = ['000000000'] * 9
    board = shapeboard(board)

    countcells = 0
    for i in range(prefill):
        # pick a random empty field and assign a random valid number
        r = sample(range(9), 1)[0]
        c = sample(range(9), 1)[0]
        if board[r][c] == 0 and possiblevalues(board, [r, c]) != []:
            arr = possiblevalues(board, [r, c])
            val = sample(arr, 1)[0]
            board[r][c] = val
            # print_difference(board, empty)
            countcells += 1
            if countcells == prefill:
                #print(board)
                solve_random(board)
                return board

def count_empty(bo):
    emptycells = 0
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                emptycells += 1
    return emptycells