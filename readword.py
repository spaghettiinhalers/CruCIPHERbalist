import numpy as np
import random
import json
import pygame as pg
from collections import OrderedDict
import nltk
import re
import unicodedata

# get_empty_clues functions: generate a list of lists, with each list corresponding to a word and the number of 0s in each list corresponding to the word length
def get_empty_a_clues(grid):
    a_clues = []
    for row in range(15):
        word = []
        for col in range(15):
            if grid[row][col] == 1:
                word.append(0)
                if col == 14:
                    a_clues.append(word)
                    word = []
            else:
                a_clues.append(word)
                word = []
    a_clues = [word for word in a_clues if word!=[]]
    return(a_clues)

def get_empty_d_clues(grid):
    d_clues = []
    for col in range(15):
        word = []
        for row in range(15):
            if grid[row][col] == 1:
                word.append(0)
                if row == 14:
                    d_clues.append(word)
                    word = []
            else:
                d_clues.append(word)
                word = []
    d_clues = [word for word in d_clues if word!=[]]
    return(d_clues)

# creates a dictionary matching the word's number to the word's length
def clue_length_dict(clues):
    cl_dict = {}
    cluenum = 0
    for clue in clues:
        length = 0
        for letter in clue:
            length += 1
        cl_dict[cluenum] = length
        cluenum += 1
    return cl_dict

# reorders dictionary so that pairs with larger values (longer words) come first, so that words can be drawn for them first
def sort_long_short(clue_lengths):
    sorted_dict = dict(OrderedDict(sorted(clue_lengths.items(), key=lambda item: item[1], reverse=True)))
    return sorted_dict