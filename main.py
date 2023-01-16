import numpy as np
import random
import json
import pygame as pg
from collections import OrderedDict
import nltk
import re
import unicodedata

import gridgen
import readword
import display
import gridcluedict
import wordlist

grid = gridgen.gen_pattern()
letter_grid = np.full((15, 15), '*')

# generates a list of lists filled with blanks to represent each letter in the empty clue
a_clues = readword.get_empty_a_clues(grid)
d_clues = readword.get_empty_d_clues(grid)

# generates a dictionary corresponding clue number and length
unsorted_a_clue_lengths = readword.clue_length_dict(a_clues)
unsorted_d_clue_lengths = readword.clue_length_dict(d_clues)

a_clue_lengths = readword.sort_long_short(unsorted_a_clue_lengths)
d_clue_lengths = readword.sort_long_short(unsorted_d_clue_lengths)

# generates a dictionary corresponding grid element location to clue element
a_grid_elements = gridcluedict.a_grid_element_dict(grid, a_clues)
d_grid_elements = gridcluedict.d_grid_element_dict(grid, d_clues)

# displays empty grid
display.display(grid)

en_wordlist = wordlist.en_wordlist()
fr_sp_wordlist = wordlist.fr_sp_wordlist()
name_wordlist = wordlist.name_wordlist()
phrase_7_list = wordlist.phrase_7_list(en_wordlist)
phrase_8_list = wordlist.phrase_8_list(en_wordlist)
phrase_9_list = wordlist.phrase_9_list(en_wordlist)
phrase_10_list = wordlist.phrase_10_list(en_wordlist)
phrase_11_list = wordlist.phrase_11_list(en_wordlist)\

num = max(len(a_clue_lengths), len(d_clue_lengths))
for i in range(num):
    # ACROSS CLUES
    if i<len(a_clue_lengths):
        clue_num = list(a_clue_lengths.keys())[i]
        # check existing cells for existing letters to implement into word search requirements:
        filled_cells = {}
        cells_occupied = []
        length = a_clue_lengths[clue_num]
        row_num = a_grid_elements[(clue_num, 0)][0]
        
        for j in range(length):
            cells_occupied.append(a_grid_elements[(clue_num, j)])
            cell_value = letter_grid[cells_occupied[j][0]][cells_occupied[j][1]]
            if cell_value != '*':
                filled_cells[j] = cell_value
        # filled_cells is now a dictionary containing what letters already exist on the grid and where in the word
        # cells_occupied is a list containing what grid cells the word occupies
        
        if len(filled_cells)!=length:
            # get word
            pot_words = [word for word in en_wordlist if len(word)==length]
            if len(pot_words)==0:
                pot_words = [word for word in fr_sp_wordlist if len(word)==length]
            if len(pot_words)==0:
                pot_words = [word for word in name_wordlist if len(word)==length]
            print(filled_cells)
            if len(filled_cells) != 0:
                for j in range(len(filled_cells)):
                    pot_words = [word for word in pot_words if word[list(filled_cells.keys())[j]]==list(filled_cells.values())[j]]
            
            if len(pot_words)!=0:
                soln = random.sample(pot_words, 1)[0]
            else:
                if length==7:
                    if len(filled_cells) != 0:
                        for j in range(len(filled_cells)):
                            pot_words = [word for word in phrase_7_list if word[list(filled_cells.keys())[j]]==list(filled_cells.values())[j]]
                    soln = random.sample(pot_words, 1)[0]
                elif length==8:
                    if len(filled_cells) != 0:
                        for j in range(len(filled_cells)):
                            pot_words = [word for word in phrase_8_list if word[list(filled_cells.keys())[j]]==list(filled_cells.values())[j]]
                    soln = random.sample(pot_words, 1)[0]
                elif length==9:
                    if len(filled_cells) != 0:
                        for j in range(len(filled_cells)):
                            pot_words = [word for word in phrase_9_list if word[list(filled_cells.keys())[j]]==list(filled_cells.values())[j]]
                    soln = random.sample(pot_words, 1)[0]
                elif length==10:
                    if len(filled_cells) != 0:
                        for j in range(len(filled_cells)):
                            pot_words = [word for word in phrase_10_list if word[list(filled_cells.keys())[j]]==list(filled_cells.values())[j]]
                    soln = random.sample(pot_words, 1)[0]
                elif length==11:
                    if len(filled_cells) != 0:
                        for j in range(len(filled_cells)):
                            pot_words = [word for word in phrase_11_list if word[list(filled_cells.keys())[j]]==list(filled_cells.values())[j]]
                    soln = random.sample(pot_words, 1)[0]
                else:
                    print(f"{length}!!!!")

            soln_list = list(soln)

            print(f"{len(soln_list)}, {len(cells_occupied)}")

            for j in range(len(cells_occupied)):
                letter_grid[cells_occupied[j][0]][cells_occupied[j][1]] = soln_list[j]
    
    # DOWN CLUES
    if i<len(d_clue_lengths):
        clue_num = list(d_clue_lengths.keys())[i]
        # check existing cells for existing letters to implement into word search requirements:
        filled_cells = {}
        cells_occupied = []
        length = d_clue_lengths[clue_num]
        col_num = d_grid_elements[(clue_num, 0)][1]
        
        for j in range(length):
            cells_occupied.append(d_grid_elements[(clue_num, j)])
            cell_value = letter_grid[cells_occupied[j][0]][cells_occupied[j][1]]
            if cell_value != '*':
                filled_cells[j] = cell_value
        # filled_cells is now a dictionary containing what letters already exist on the grid and where in the word
        # cells_occupied is a list containing what grid cells the word occupies
        
        if len(filled_cells)!=length:
            # get word
            pot_words = [word for word in en_wordlist if len(word)==length]
            if len(pot_words)==0:
                pot_words = [word for word in fr_sp_wordlist if len(word)==length]
            if len(pot_words)==0:
                pot_words = [word for word in name_wordlist if len(word)==length]
            print(filled_cells)
            if len(filled_cells) != 0:
                for j in range(len(filled_cells)):
                    pot_words = [word for word in pot_words if word[list(filled_cells.keys())[j]]==list(filled_cells.values())[j]]
            
            if len(pot_words)!=0:
                soln = random.sample(pot_words, 1)[0]
            else:
                if length==7:
                    if len(filled_cells) != 0:
                        for j in range(len(filled_cells)):
                            pot_words = [word for word in phrase_7_list if word[list(filled_cells.keys())[j]]==list(filled_cells.values())[j]]
                    soln = random.sample(pot_words, 1)[0]
                elif length==8:
                    if len(filled_cells) != 0:
                        for j in range(len(filled_cells)):
                            pot_words = [word for word in phrase_8_list if word[list(filled_cells.keys())[j]]==list(filled_cells.values())[j]]
                    soln = random.sample(pot_words, 1)[0]
                elif length==9:
                    if len(filled_cells) != 0:
                        for j in range(len(filled_cells)):
                            pot_words = [word for word in phrase_9_list if word[list(filled_cells.keys())[j]]==list(filled_cells.values())[j]]
                    soln = random.sample(pot_words, 1)[0]
                elif length==10:
                    if len(filled_cells) != 0:
                        for j in range(len(filled_cells)):
                            pot_words = [word for word in phrase_10_list if word[list(filled_cells.keys())[j]]==list(filled_cells.values())[j]]
                    soln = random.sample(pot_words, 1)[0]
                elif length==11:
                    if len(filled_cells) != 0:
                        for j in range(len(filled_cells)):
                            pot_words = [word for word in phrase_11_list if word[list(filled_cells.keys())[j]]==list(filled_cells.values())[j]]
                    soln = random.sample(pot_words, 1)[0]
                else:
                    print(f"{length}!!!!")

            soln_list = list(soln)

            print(f"{len(soln_list)}, {len(cells_occupied)}")

            for j in range(len(cells_occupied)):
                letter_grid[cells_occupied[j][0]][cells_occupied[j][1]] = soln_list[j]
    
    # print(letter_grid)

# prints completed crossword layout
print(letter_grid)

# displays empty grid again
display.display(grid)