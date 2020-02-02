""" 
Project 1.1: Indonesian Dot Puzzle Board Class
COMP 472 NN 
DUE: Feb 9th, 2020
Samantha Yuen (40033121), Andrew Marcos (40011252), Michael Gagnon (40030481)

Purpose:
IO setup file to import the indonesian puzzle input.txt file and create a list of Boards.

Methods:
  createBoards(input) -- takes a string containing the input file name, outputs a list of Board puzzle (1 Board line)
  atGoal(Board) -- takes a Board state as input and outputs a boolean. True if all values are 0, False otherwise
  
PUT IN DFS:
  sortChildren(Boards) -- takes a list of board states and reorders them according to the position of zeroes. 
"""

num = 0

with open('test.txt','r') as f:

  puzzle_contents= f.read()
  print(puzzle_contents)

with open('test.txt','r') as f:

  for line in f:
    num += 1
  print("There is:", num, " Puzzles")
  
  


  def atGoal(state):
    for row in state:   # loop through each value in the board's state (2D array)
      for val in row:
        if val != 0:
          return False  # if there is a single 1 in the matrix return False
    return True         # otherwise return True
