from constraint import *
from board import *
import copy
from random import shuffle

backtracker = 0
backtrackerrand = 0
count = 0
row_old = 0
bo_old = []
bo_old_old = []
flag_stuck = 0
bo_stuck = []
hist = []

board_old = copy.deepcopy([])
def solve(bo):

    global count
    global hist
    global board_old

    find = find_empty(bo)
    hist.append(find)
    count = count + 1
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if constraintsatisfaction(bo, i, (row, col)):
            bo[row][col] = i


            if solve(bo):
                return True

            #print('backtracking')
            #print_difference(board_old, bo)
            board_old = copy.deepcopy(bo)
            bo[row][col] = 0


    return False

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None


def solve_difficulty(bo, difficulty=10):
    global backtracker
    global count
    global hist
    global board_old
    find = find_empty(bo)
    hist.append(find)
    count = count + 1
    if not find:
        return True
    else:
        row, col = find

    ls = list(range(0, 10))
    shuffle(ls)
    for i in ls:
        if constraintsatisfaction(bo, i, (row, col)):
            bo[row][col] = i

            if solve_random(bo):
                return True

            #print('backtracking')
            # print_difference(board_old, bo)
            if backtracker >= difficulty:
                return False
            backtracker += 1
            board_old = copy.deepcopy(bo)
            bo[row][col] = 0
    backtracker += 1
    if backtracker >= difficulty:
        return False
    return False


def solve_random(bo):
    global count
    global hist
    global board_old
    global backtrackerrand

    find = find_empty(bo)
    hist.append(find)
    count = count + 1
    if not find:
        return True
    else:
        row, col = find

    ls = list(range(0, 10))
    shuffle(ls)
    for i in ls:
        if constraintsatisfaction(bo, i, (row, col)):
            bo[row][col] = i

            if solve_random(bo):
                return True

            if backtrackerrand >= 50000:
                return False
            # print('backtracking')
            # print_difference(board_old, bo)
            board_old = copy.deepcopy(bo)
            bo[row][col] = 0
    if backtrackerrand >= 50000:
        return False
    return False