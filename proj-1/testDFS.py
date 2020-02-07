from DFS import DFS
from board import Board
import time

start_time = time.time()

test = Board(1, 4, 10, '1110011001111001100111100110011110011001111001100111100110011110011001111001100111100110011110011001')
dfs = DFS()


dfs.dfsSearch(test)

print("--- %s seconds ---" % (time.time() - start_time))
