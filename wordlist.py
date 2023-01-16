import numpy as np
import random
import json
import pygame as pg
from collections import OrderedDict
import nltk
import re
import unicodedata

# removes some words with odd structure that would make them more difficult to incorporate into a crossword
def filter_words(word_list):
    filtered_word_list = []
    for word in word_list:
        vowels = len(re.findall('[aeiou]', word))
        consonants = len(re.findall('[bcdfghklmnprstvwy]', word))
        bad = len(re.findall('[jqxz]', word)) # removes words with the 4 least-used letters in English
        if (consonants==0 or vowels/consonants>=1/3) and bad==0: # requires a certain number of vowels
            filtered_word_list.append(word)
    return filtered_word_list

# removes accents from french and spanish words
def remove_accents(word):
    word = unicodedata.normalize('NFD', word)
    word = "".join([c for c in word if unicodedata.category(c) != 'Mn'])
    return word

def en_wordlist():
    nltk.download('words')
    word_list = nltk.corpus.words.words()
    
    en_wordlist = filter_words(word_list)
    return en_wordlist

def fr_sp_wordlist():
    nltk.download('cess_esp')
    word_list = nltk.corpus.cess_esp.words()
    no_accent_list = [remove_accents(word) for word in word_list]

    fr_sp_wordlist = filter_words(word_list)
    return fr_sp_wordlist

def name_wordlist():
    nltk.download('names')
    word_list = nltk.corpus.names.words()

    name_wordlist = filter_words(word_list)
    return name_wordlist

# phrase functions combine two words to come up with a phrase of a certain length as a last-resort word
def phrase_7_list(en_wordlist):
    list_3 = [word for word in en_wordlist if len(word)==3]
    list_4 = [word for word in en_wordlist if len(word)==4]
    phrase_7_list = []

    for i in range(len(list_3)):
        for j in range(len(list_4)):
            phrase = list_3[i]
            phrase += list_4[j]
            phrase_7_list.append(phrase)
            
    return phrase_7_list

def phrase_8_list(en_wordlist):
    list_3 = [word for word in en_wordlist if len(word)==3]
    list_5 = [word for word in en_wordlist if len(word)==5]
    phrase_8_list = []

    for i in range(len(list_3)):
        for j in range(len(list_5)):
            phrase = list_3[i]
            phrase += list_5[j]
            phrase_8_list.append(phrase)
            
    return phrase_8_list

def phrase_9_list(en_wordlist):
    list_4 = [word for word in en_wordlist if len(word)==4]
    list_5 = [word for word in en_wordlist if len(word)==5]
    phrase_9_list = []

    for i in range(len(list_4)):
        for j in range(len(list_5)):
            phrase = list_4[i]
            phrase += list_5[j]
            phrase_9_list.append(phrase)
            
    return phrase_9_list

def phrase_10_list(en_wordlist):
    list_4 = [word for word in en_wordlist if len(word)==4]
    list_6 = [word for word in en_wordlist if len(word)==6]
    phrase_10_list = []

    for i in range(len(list_4)):
        for j in range(len(list_6)):
            phrase = list_4[i]
            phrase += list_6[j]
            phrase_10_list.append(phrase)
            
    return phrase_10_list

def phrase_11_list(en_wordlist):
    list_5 = [word for word in en_wordlist if len(word)==5]
    list_6 = [word for word in en_wordlist if len(word)==6]
    phrase_11_list = []

    for i in range(len(list_5)):
        for j in range(len(list_6)):
            phrase = list_5[i]
            phrase += list_6[j]
            phrase_11_list.append(phrase)
            
    return phrase_11_list