from constraint import *
from board import *

import copy


def solveminarray(board, printenable):
    dic_old = 81
    board_old = copy.deepcopy(board)

    step = 0
    while minarray(board):
        step += 1
        #if printenable == 1:
            #print("board after step", step)
            #print_difference(board, board_old)
        board_old = copy.deepcopy(board)
        minarray(board)

        if len(dic) < dic_old:
            dic_old = len(dic)
            minarray(board)
        else:
            break

def minarray(board):
    global dic
    dic = {}
    for i in range(len(board)):
            for j in range(len(board[0])):
                row = i
                col = j
                pos = [i, j]
                if board[i][j] == 0:
                    possiblevalues = []
                    for val in range (1,10):
                        if constraintsatisfaction(board, val, pos):
                            #print(constraintsatisfaction(board, i, emptycell))
                            possiblevalues.append(val)
                    if len(possiblevalues) == 1:
                        board[i][j] = possiblevalues[0]
                    else:
                        dic.update( {(str(row),str(col)): possiblevalues})
    if dic == {}:
        return False
    else:
        return True