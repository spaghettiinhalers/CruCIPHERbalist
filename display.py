import numpy as np
import random
import json
import pygame as pg
from collections import OrderedDict
import nltk
import re
import unicodedata

# display black/white cell pattern
def display(grid):
    pg.init()
    window_size = (450, 450)
    screen = pg.display.set_mode(window_size)
    pg.display.set_caption("Crossword")

    cell_size = int(window_size[0] / 15)

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        screen.fill((255, 255, 255))
        for y in range(15):
            for x in range(15):
                if grid[y][x] == 0:
                    color = (0,0,0)
                else:
                    color = (255,255,255)
                pg.draw.rect(screen, color, (x * cell_size, y * cell_size, cell_size, cell_size))
                pg.draw.line(screen, (0, 0, 0), (x*cell_size, 0), (x*cell_size, 450), 1)
            pg.draw.line(screen, (0, 0, 0), (0, y*cell_size), (450, y*cell_size), 1)

        # Update the display
        pg.display.flip()

    # Quit pg
    pg.quit()