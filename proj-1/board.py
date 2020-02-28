import numpy as np  # for 2D array
import copy  # see touch() function
import random

""" 
Project 1.1: Indonesian Dot Puzzle Board Class
COMP 472 NN 
DUE: Feb 9th, 2020
Samantha Yuen (40033121), Andrew Marcos (40011252), Michael Gagnon (40030481) 

Purpose:
The Board class holds the object Board representing the Indonesian puzzle's state. 

Object Variables:
    num (puzzle number)
    size (dimension of puzzle)
    state (values in puzzle (by row))
    maxD (maximum depth)

Object Variables used by:
    DFS: maxD (maximum depth)

Constructor takes in parameters num, maxD, size and state creates objects of varying board sizes 3x3 to 10x10 grids

Object Methods:
    touch(self, coord) -- flips values of puzzle given coordinate as input
    visualState(self) -- prints state as 2D array
    printState(self) -- prints state as a string
    printInvertedState(self) --- prints state as a string with bits inverted for sorting purposes
    compare(self, otherBoard) -- compare self board with other board. If equal return true, otherwise return false

Class Method
    convertCoord(cls, coord) -- with an input string of length = 2, it is converted to a list containing
                                the row position index[0] and column position index[1]. It is used in touch() object method.
    flip(tile) -- with an input of 1 or 0, return the opposite, 1 or 0.

Free Method
    heuristicValue(board) -- with an input of a board and type (of heuristic), return the estimated cost to reach the goal from current state
"""


""" Free Methods """

# def heuristicValue(board):
#     # TODO: Replace this random number with the heurstic value determining of the board
#     return random.randint(1, 40)        
heuristicOption = 3

def heuristicValue(board, type):
    # type 1: simple heuristic similar to DFS bubble sort to prioritize 0s. Goal state = 0; Max value = 45
    # type 2: heuristic that weights each position by if there is a 1. If it is surrounded by 1s, the weight of the position decreases
    # type 3: heuristic combines type 1 and type 2 where each position has a weight and is informed about the surrounding tiles
    
    heuristic = 0
    if (type == 1):
        counter = 1 # Goal state h(n) = 0
        # Iterate through the board state
        for value in np.nditer(board.state):
            heuristic += value*counter
            counter += 1
        return heuristic

    elif (type == 2):
        heuristic = 0 # Goal state h(n) = 0
        # Iterate through each position in the board state
        for row in range(0,board.size):
            for col in range(0, board.size):
                if (board.state[row, col] == 1):
                    heuristic += 1
                    # Check the top value, if we're not at the top row
                    if (row > 0):
                        if (board.state[row-1, col] == 1):
                            heuristic +=1
                    #Check the bottom value, we're not at the bottom row
                    if (row < board.size-1):
                        if (board.state[row+1, col] == 1):
                            heuristic +=1
                    # Check the left value, we're not at the left-most column
                    if (col > 0):
                        if (board.state[row, col-1] == 1):
                            heuristic +=1
                    #Check the right value, we're not at the right-most column
                    if (col < board.size-1):
                        if (board.state[row, col+1] == 1):
                            heuristic +=1
        return heuristic

    elif (type == 3):
        heuristic = 0 # Goal state h(n) = 0
        counter = 0
        # Iterate through each position in the board state
        for row in range(0,board.size):
            for col in range(0, board.size):
                counter += 1 # ranges from 1 to size*size
                if (board.state[row, col] == 1):
                    heuristic += counter #include the weight of the position
                     # Check the top value, if we're not at the top row
                    if (row > 0):
                        if (board.state[row-1, col] == 1):
                            heuristic +=1
                    #Check the bottom value, we're not at the bottom row
                    if (row < board.size-1):
                        if (board.state[row+1, col] == 1):
                            heuristic +=1
                    # Check the left value, we're not at the left-most column
                    if (col > 0):
                        if (board.state[row, col-1] == 1):
                            heuristic +=1
                    #Check the right value, we're not at the right-most column
                    if (col < board.size-1):
                        if (board.state[row, col+1] == 1):
                            heuristic +=1
        return heuristic

    else:
        return ("Invalid parameters entered, please choose heuristic type 1, 2, or 3")


""" Board Class """

class Board:

    """Constructor"""

    def __init__(self, num, maxD, size, state, maxL):
        self.num = int(num)   # index of puzzle
        self.maxD = int(maxD)  # maximum depth (for Depth-First Search)
        self.maxL = int(maxL)
        self.size = int(size)  # Size of the puzzle (3-10)
        if (isinstance(state, str)):
            state_splitted = [int(digit) for digit in state]
            # Split the values (int) of the board into an array of 1s and 0s
            self.state = np.array(state_splitted).reshape(int(size), int(size))
            # Store the board state (by row) as a size by size ndarray
        else:
            self.state = state  # copies state from another board

    """Object Methods"""

    def touch(self, coord):
        index = Board.convertCoord(coord)   # Convert the string coord of length 2 to a list of length 2 holding the row and column as ints

        if (index[0] >= self.size or index[1] >= self.size):
            return print("Coordinates out of Bounds")

        # Initiate a new Board object using the old Board (self)
        # uses deepcopy method from copy library
        newBoard = Board(copy.deepcopy(self.num),
                         copy.deepcopy(self.maxD),
                         copy.deepcopy(self.size),
                         copy.deepcopy(self.state),
                         copy.deepcopy(self.maxL))

        # Flip the index value
        if (newBoard.state[index[0], index[1]] == 1):
            newBoard.state[index[0], index[1]] = 0
        else:
            newBoard.state[index[0], index[1]] = 1

        # Flip the top value
        if index[0] > 0:  # if we're not at the top row, flip the top value
            if (newBoard.state[index[0]-1, index[1]] == 1):
                newBoard.state[index[0]-1, index[1]] = 0
            else:
                newBoard.state[index[0]-1, index[1]] = 1

        # Flip the bottom value
        if index[0] < newBoard.size-1:  # if we're not at the bottom row, flip the bottom value
            if (newBoard.state[index[0]+1, index[1]] == 1):
                newBoard.state[index[0]+1, index[1]] = 0
            else:
                newBoard.state[index[0]+1, index[1]] = 1

        # Flip the left value
        if index[1] > 0:  # if we're not at the left-most column, flip the left value
            if (newBoard.state[index[0], index[1]-1] == 1):
                newBoard.state[index[0], index[1]-1] = 0
            else:
                newBoard.state[index[0], index[1]-1] = 1

        # Flip the right value
        if index[1] < newBoard.size-1:  # if we're not at the right-most column, flip the right value
            if (newBoard.state[index[0], index[1]+1] == 1):
                newBoard.state[index[0], index[1]+1] = 0
            else:
                newBoard.state[index[0], index[1]+1] = 1

        return newBoard

    def visualState(self):
        # Return a 2D array of the board state
        return self.state

    def printState(self):
        #EX: 101010101
        result = ""                     # Create an empty string
        for row in self.state:
            for val in row:             # Loop through each value in the 2D matrix
                # Append each value into a result string
                result = result + str(val)
        return result

    def printInvertedState(self):
        # The same functioning as before, except the 0s and 1s are inverted (for sorting purposes)
        result = ""                     # Create an empty string
        for row in self.state:
            for val in row:             # Loop through each value in the 2D matrix
                # Append each value into a result string
                result = result + str(self.flip(val))
        return result
    
    @classmethod
    def flip(cls, tile):
        # Returned value is passed in getInverseValue for sorting 
        if(tile == 1):
            return 0
        else:
            return 1

    def compare(self, otherBoard):
        # return true if the state of both boards are equal, otherwise return false
        if self.size != otherBoard.size:
            return False
        else:
            for row in range(0, self.size):
                for col in range(0, self.size):
                    if self.state[row, col] != otherBoard.state[row, col]:
                        return False
        return True

    @classmethod
    def convertCoord(cls, coord):
        # coord parameter is a string of length two indicating the row (A-J) and column (1-10)
        # Outputs an array of length 2 containing the row (x-axis) as a letter and column (y-axis) as an integer
        position = []
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
        position = [row.get(coord[0], -1), int(coord[1:len(coord)])-1]
        # convert the row letter to an integer (e.g A = 0), and the second char as an int of the column
        return position