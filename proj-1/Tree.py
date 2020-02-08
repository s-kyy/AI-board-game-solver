"""
Project 1.1: Depth First Search Algorithm
COMP 472 NN 
DUE: Feb 9th, 2020
Samantha Yuen (40033121), Andrew Marcos (40011252), Michael Gagnon (40030481)

Purpose:
The Tree class is the data structure used by DFS

Object Variables:
    head (puzzle number)
    openlist (dimension of puzzle)
    closedlist (values in puzzle (by row))

Constructor takes in the head node and creates an empty open and closed list.
"""


class Tree:
    def __init__(self, head):
        self.head = head
        self.openlist = []
        self.closedlist = {}
