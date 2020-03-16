from boardbuilder import *

import copy

fixed_hist = []
for q in range(1):
    try:
        b = 0
        while not isinstance(b, list):
            b = build_board(5)
        print("________solved board_______")
        print_board(b)

        brd = copy.deepcopy(b)

        remove(brd, 10)
        removed = count_empty(brd)
        fixed_hist.append(81-removed)
        print("_____reduced board______")
        print("___(",81-removed,"cells fixed)___")
        print_board(brd)
        probasstring = reshapeboard(brd)

        solve(brd)
        soluasstring = reshapeboard(brd)
        print('success')
        #print("________solved board after reduction_______")
        #print_board(brd)
    except:
        print('except')
        continue
print(fixed_hist)

with open('creator.txt', 'w') as f:
    f.write(probasstring)
    f.write(',')
    f.write(soluasstring)