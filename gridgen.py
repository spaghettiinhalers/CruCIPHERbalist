import numpy as np
import random
import json
import pygame as pg
from collections import OrderedDict
import nltk
import re
import unicodedata

# randomly generates placement of black cells in a 15-cell line
def get_edge_blacks():
    x = random.randint(1, 3)
    if x == 1:
        blacks = [3, 5, 5] # white cell options
    elif x == 2:
        blacks = [4, 4, 5]
    elif x == 3:
        blacks = [3, 4, 6]
    random.shuffle(blacks)
    return blacks

def gen_pattern():
    grid = np.ones((15, 15)) # generate empty crossword grid
    blacks_left = 36 # updated as black cells are placed

    # sets black cells on edges
    tb1 = random.randint(1, 3) # chooses random length of black cells, up to 3 spaces
    tb2 = random.randint(1, 3)
    lr1 = random.randint(1, 3)
    lr2 = random.randint(1, 3)

    tb_blacks = get_edge_blacks()
    for i in range(tb1):
        grid[i][tb_blacks[0]] = 0 # starts on edge and moves in
        blacks_left -= 1 # for each black placed, update number of black cells left
    for i in range(tb2):
        grid[i][tb_blacks[0] + tb_blacks[1] + 1] = 0
        blacks_left -= 1
    for i in range(tb1):
        grid[14-i][tb_blacks[2] + tb_blacks[1] + 1] = 0
        blacks_left -= 1
    for i in range(tb2):
        grid[14-i][tb_blacks[2]] = 0
        blacks_left -= 1

    lr_blacks = get_edge_blacks()
    for i in range(lr1):
        grid[lr_blacks[0]][i] = 0
        blacks_left -= 1
    for i in range(lr2):
        grid[lr_blacks[0] + lr_blacks[1] + 1][i] = 0
        blacks_left -= 1
    for i in range(lr1):
        grid[lr_blacks[2] + lr_blacks[1] + 1][14-i] = 0
        blacks_left -= 1
    for i in range(lr2):
        grid[lr_blacks[2]][14-i] = 0
        blacks_left -= 1

    # set black cells in the inner rectangle
    tb_max = max(tb1, tb2)
    lr_max = max(lr1, lr2)

    inner_columns = []
    for column in range(lr_max+1, 15-lr_max):
        inner_columns.append(column)
    random.shuffle(inner_columns)
    inner_rows = []
    for row in range(tb_max, 15-tb_max):
        inner_rows.append(row)
    random.shuffle(inner_rows)

    while np.count_nonzero(grid == 1)>189:
        if np.count_nonzero(grid == 1)==190:
            num = random.choice([x for x in inner_columns if x in inner_rows])
            grid[num][num] = 0
        else:
            cnum = random.choice(inner_columns)
            rnum = random.choice(inner_rows)
            if grid[rnum][cnum]==1 and cnum!=rnum and grid[cnum][rnum]==1:
                grid[rnum][cnum] = 0
                grid[14-rnum][14-cnum] = 0

    return grid