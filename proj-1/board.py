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
import numpy as np # for 2D array
import copy # see touch() function

class Board:
    

    """Constructor"""
    def __init__(self, num, maxD, size, state):
        self.num    = num   # index of puzzle
        self.maxD   = maxD  # maximum depth (for Depth-First Search)
        self.size   = size  # Size of the puzzle (3-10)
        if (isinstance(state, str)):
            state_splitted = [int(state[i]) for i in range(0,len(state), 1)] 
                            # Split the values (int) of the board into an array of 1s and 0s
            self.state = np.array(state_splitted).reshape(size, size)
                            # Store the board state as a size by size ndarray
        else:
            self.state = state # copies state from another board


    """Object Methods"""
    # touch(seld, coord) -- flips values of puzzle given coordinate as input
    # visualState(self) -- prints state as 2D array
    # printState(self) -- prints state as a string
    # compare(self, otherBoard) -- compare self board with other board. If equal return true, otherwise return false

    def touch(self, coord): 
        index = Board.convertCoord(coord)
        # print(str(coord[0]) + str(coord[1]) + " -> " + str(index[0]) + str(index[1]))

        if (index[0] >= self.size or index[1] >= self.size):
            return print("Coordinates out of Bounds")

        # Initiate a new Board object using the old Board (self)
        # uses deepcopy method from copy library
        newBoard = Board(copy.deepcopy(self.num), 
                         copy.deepcopy(self.maxD), 
                         copy.deepcopy(self.size), 
                         copy.deepcopy(self.state))

        # print("Original Board")
        # print(self.visualState())

        # Flip the index value
        if (newBoard.state[index[0], index[1]] == 1):
            newBoard.state[index[0], index[1]] = 0
        else:
            newBoard.state[index[0], index[1]] = 1

        # print("Flip index value")
        # print(newBoard.visualState())

        # Flip the top value
        print(index[0] > 0)
        if index[0] > 0: #if we're not at the top row, flip the top value
            if (newBoard.state[index[0]-1, index[1]] == 1):
                newBoard.state[index[0]-1, index[1]] = 0
            else:
                newBoard.state[index[0]-1, index[1]] = 1

        # print("Flip top value")
        # print(newBoard.visualState())

        # Flip the bottom value
        if index[0] < newBoard.size-1: #if we're not at the bottom row, flip the bottom value
            print(newBoard.state[index[0]+1, index[1]] == 1)
            if (newBoard.state[index[0]+1, index[1]] == 1):
                newBoard.state[index[0]+1, index[1]] = 0
            else:
                newBoard.state[index[0]+1, index[1]] = 1

        # print("Flip bottom value")
        # print(newBoard.visualState())

        # Flip the left value
        print(index[1] > 0)
        if index[1] > 0: #if we're not at the left-most column, flip the left value
            if (newBoard.state[index[0], index[1]-1] == 1):
                newBoard.state[index[0], index[1]-1] = 0
            else:
                newBoard.state[index[0], index[1]-1] = 1

        # print("Flip left value")
        # print(newBoard.visualState())

        # Flip the right value
        if index[1] < newBoard.size-1: #if we're not at the right-most column, flip the right value
            if (newBoard.state[index[0], index[1]+1] == 1):
                newBoard.state[index[0], index[1]+1] = 0
            else:
                newBoard.state[index[0], index[1]+1] = 1

        # print("New Board")
        # print(newBoard.visualState())
        return newBoard

    def visualState(self):
        # Return a 2D array of the board state
        return self.state
        
    def printState(self):
        #EX: 101010101
        result = ""                     # Create an empty string
        for row in self.state:
            for val in row:             # Loop through each value in the 2D matrix
                result = result + val   # Append each value into a result string
        return result

    def compare(self, otherBoard):
        # return true if the state of both boards are equal, otherwise return false
        if self.size != otherBoard.size:
            return False
        else:
            for row in range(0, self.size) :
                for col in range(0, self.size) :
                    if self.state[row, col] != otherBoard.state[row, col]:
                        return False
        return True

    @classmethod
    def convertCoord(cls, coord):
        position = []   # array of length 2 containing the row (x-axis) and column (y-axis) of Board 2D array 
        row = {         # dictionary of letters corresponding to row ints
            'A': 0,
            'B': 1,
            'C': 2,
            'D': 3,
            'E': 4,
            'F': 5,
            'G': 6,
            'H': 7,
            'I': 8,
            'J': 9
        }
        position = [row.get(coord[0],-1),int(coord[1:len(coord)])-1]
                        # convert the letter to a row number (e.g A = 1), and the second char as an int of the column 
        return position