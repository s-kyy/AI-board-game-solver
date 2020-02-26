from setup import returnBoards
from dfs import DFS
from bestfirst import BestFirstSearch
from astar import AStarSearch
import time

""" 
Project 1.1: Indonesian Dot Puzzle Board Class
COMP 472 NN 
DUE: Feb 9th, 2020
Samantha Yuen (40033121), Andrew Marcos (40011252), Michael Gagnon (40030481) 

This file is responsible for starting all three searches on the board test file.
"""

filename = input("Enter filename with board setup:")
listOfBoards = returnBoards(filename)
dfs = DFS()
bfs = BestFirstSearch()
afs = AStarSearch()

for board in listOfBoards:
    #input('enter to continue')
    start_time = time.time()
    dfs.dfsSearch(board)
    print("--- Board #%s finished in %s seconds for dfs ---" %
          (board.num, time.time() - start_time))
    start_time = time.time()
    bfs.bestFirstSearch(board)
    print("--- Board #%s finished in %s seconds for bfs ---" %
          (board.num, time.time() - start_time))
    start_time = time.time()
    afs.aStarSearch(board)
    print("--- Board #%s finished in %s seconds for a* ---" %
          (board.num, time.time() - start_time))
