# CruCIPHERbalist
NYT Crossword Puzzle Generator

The pattern generation algorithm follows the NYT's Mon/Tue/Wed/Thu crossword rules. The standard puzzle is a 15x15 grid with a black:white cell ratio of 36:189 with rotational symmetry. The density of the white cells and specifications regarding black cell placement make these puzzles more difficult to generate than regular crossword puzzles.

NOTE: Currently, my algorithm does not entirely follow NYT crossword conventions - there is a small problem with the pattern generation code that results in the existence of words that are 1-2 letters in length. This will be fixed when I am less tired.

Future Improvements (in order of how soon I can make them):
 - fix aforementioned pattern generation bug
 - turn program into a functional game with an interactive grid and solution-checking
 - allow messages to be hidden in the puzzle (I like puns and I started this project because of the great pun I thought of for the title, so I need to incorporate the "cipher" part of it as soon as possible)

Possible Future Improvements:
 - incorporate NLP to generate clues, nuanced themes, and solutions of higher quality in general (enormous liberties were taken when considering what counted as an acceptable "word")
 - expand the program's abilities to create puzzles of Fri/Sat/Sun-level complexity
