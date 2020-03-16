from textwrap import wrap
from termcolor import colored

def shapeboard(sud_prob):
    bo = [None]*9
    i = 0
    for row in sud_prob:
        rowaslist = wrap(row,1)
        rowaslist = list(map(int, rowaslist))
        bo[i] = rowaslist
        i = i + 1
    return bo

def reshapeboard(bo):
    out = list()
    for i in bo:
        for j in i:
            out.append(str(j))
    return ''.join(out)

def takeproblem(srcfile, linenumber):
    return wrap(srcfile[linenumber].split(',')[0], 9)

def takesolution(srcfile, linenumber):
    return srcfile[linenumber].split(',')[1]

def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

def print_difference(boprint, bocomparison):
    for i in range(len(boprint)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(boprint[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                if boprint[i][j] == bocomparison[i][j]:
                    print(colored(str(boprint[i][j])))
                else:
                    print(colored(str(boprint[i][j]), on_color='on_green'))

            else:
                if boprint[i][j] == bocomparison[i][j]:
                    print(colored(str(boprint[i][j])) + " ", end="")
                else:
                    print(colored(str(boprint[i][j]), on_color='on_green') + " ", end="")
