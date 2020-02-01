""" 
Project 1.1: Indonesian Dot Puzzle Board Class
COMP 472 NN 
DUE: Feb 9th, 2020
Samantha Yuen (40033121), Andrew Marcos (40011252), Michael Gagnon (40030481)

Variables include: max_d (depth), max_l (search path length)
Constructors that takes in input file and creates objects of varying board sizes 3x3, 4x4 and 5x5 grids
Methods to modify tokens on the board adjacent to input coordinates 
Method to return if game is finished (all 0s)
Method to return number of 1s on the board (for heuristic function?)
Method to return the coordinates of 1s on the board (heursitic function)
"""
import numpy as np

class Board:
    
    """Constructors"""
    def __init__(self, num, maxD, size, state):
        self.number = num   # index of puzzle
        self.maxD = maxD    # maximum depth (for Depth-First Search)
        self.size = size    # Size of the puzzle (3-10)
        if (isinstance(state, str)):
            state_splitted = [state[i] for i in range(0,len(state), 1)] 
                            # Split the content of the board into an array of 1s and 0s
        self.state = np.array(state_splitted).reshape(size, size)
                            # Store the board state as a size by size ndarray


    """Methods"""
    def touch(coord): 
        pass

    # def visualize():
    #     pass

    def toString(self):
        #EX: 0 0 0 101010101
        result = self.state
        return result

    # def is_equal(self, Board):
    #     pass

    def convertCoord(coord):
        # switch = {
        #     'A': 0
        #     'B': 
        # }
        pass