import os
import sys
from board import Board
""" 
Project 1.1: Indonesian Dot Puzzle Board Class
COMP 472 NN 
DUE: Feb 9th, 2020
Samantha Yuen (40033121), Andrew Marcos (40011252), Michael Gagnon (40030481)

Purpose:
IO setup file to import the indonesian puzzle input.txt file and create a list of Boards.

Methods:
  returnBoards(input) -- takes a string containing the input file name, returns list of boards
  atGoal(Board) -- takes a Board state as input and outputs a boolean. True if all values are 0, False otherwise
"""


def returnBoards(inputfile):
    # Pass a string of the input file, returns a list of the file's boards
    boardList = []
    counter = 0
    if(not os.path.isfile(inputfile)):
        print('File doesnt exist, terminating program...')
        sys.exit()
    with open(inputfile, 'r') as f:
        for line in f:
            words = line.split()
            boardList.append(
                Board(counter, words[1], words[0], words[3]))
            counter += 1
    return boardList


def atGoal(state):
    # loop through each value in the board's state (2D array)
    for row in state:
        for val in row:
            if val != 0:
                return False  # if there is a single 1 in the matrix return False
    return True         # otherwise return True
