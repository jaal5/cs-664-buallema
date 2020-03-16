from board import *
from brute import *
from constraint import *
from minarray import *

import datetime
import copy

if __name__ == '__main__':

    ### read the file
    # read sudoku file
    filepath = "C:\\Users\\s-jallemann\\Documents\\CS-664-ArtificialIntelligence\\"
    # filename = "kaggle-sudoku-errorfile.txt"
    #filename = "hardestsudoku.txt"
    filename = "kaggle-sudoku.txt"
    file = filepath + filename
    print("loading", file)
    srcfile = open(file, "r")
    srcfile = srcfile.read().split("\n")

    ###


    durationtotal = datetime.timedelta()
    durations = list()

    errorcount = 0
    printenable = 1
    for linenumber in range(1, 2):
        sud_prob = takeproblem(srcfile, linenumber)
        sud_solu = takesolution(srcfile, linenumber)
        #print('solution from file: ',sud_solu)
        board = shapeboard(sud_prob)

        start = datetime.datetime.now()
        if printenable == 1:
            print("________problem________")
            print_board(board)

        #solve(board)
        solveminarray(board, printenable)

        if printenable == 1:
            print("________solution_______")
            print_board(board)

        end = datetime.datetime.now()
        duration = end - start

        durations.append(duration)
        durationtotal = durationtotal + duration

        solutionaslist = reshapeboard(board)
        #print('solution from calculation: ', solutionaslist)
        checksum = int(solutionaslist) - int(sud_solu)

        with open('durations_2.txt', 'a') as f:
            f.write(str(duration))
            f.write('\n')

        if checksum != 0:
            print('error at problem', linenumber)
            errorcount += 1
            continue

        if linenumber % 1 == 0:
            print((1-(errorcount/(linenumber+1)))*100, 'percent of', linenumber , 'problems solved correctly in', durationtotal)

    print('errorcounter: ', errorcount)


