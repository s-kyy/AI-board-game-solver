from setup import returnBoards
from dfs import DFS
import time

""" 
Project 1.1: Indonesian Dot Puzzle Board Class
COMP 472 NN 
DUE: Feb 9th, 2020
Samantha Yuen (40033121), Andrew Marcos (40011252), Michael Gagnon (40030481) 
"""

filename = input("Enter filename with board setup:")
listOfBoards = returnBoards(filename)
dfs = DFS()

for board in listOfBoards:
    #input('enter to continue')
    start_time = time.time()
    dfs.dfsSearch(board)
    print("--- Board #%s finished in %s seconds ---" %
          (board.num, time.time() - start_time))
