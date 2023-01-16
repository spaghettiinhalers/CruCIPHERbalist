import numpy as np
import random
import json
import pygame as pg
from collections import OrderedDict
import nltk
import re
import unicodedata

# GRID_ELEMENT DICTIONARIES - assign elements in grid[][] to elements in clues[][]
# across
def a_grid_element_dict(grid, a_clues):
    a_grid_elements = {}
    a, b, c, d = 0, 0, 0, 0
    while grid[a][b]==1 and a_clues[c][d]==0:    
        grid_dims_tup = (a, b)
        a_clue_dims_tup = (c, d)
        a_grid_elements[a_clue_dims_tup] = grid_dims_tup
        b += 1
        d += 1
        if d==len(a_clues[c]):
            c += 1
            d = 0
        if b==15:
            a += 1
            b = 0
        if c==len(a_clues) or a==15:
            break
        while grid[a][b]==0:
            b += 1
            if b==15:
                a += 1
                b = 0
    return a_grid_elements

# down
def d_grid_element_dict(grid, d_clues):    
    d_grid_elements = {}
    a, b, c, d = 0, 0, 0, 0
    while grid[a][b]==1 and d_clues[c][d]==0:    
        grid_dims_tup = (a, b)
        d_clue_dims_tup = (c, d)
        d_grid_elements[d_clue_dims_tup] = grid_dims_tup
        a += 1
        d += 1
        if d==len(d_clues[c]):
            c += 1
            d = 0
        if a==15:
            b += 1
            a = 0
        if c==len(d_clues) or b==15:
            break
        while grid[a][b]==0:
            a += 1
            if a==15:
                b += 1
                a = 0
    return d_grid_elements