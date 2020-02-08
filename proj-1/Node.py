"""
Project 1.1: Depth First Search Algorithm
COMP 472 NN 
DUE: Feb 9th, 2020
Samantha Yuen (40033121), Andrew Marcos (40011252), Michael Gagnon (40030481)

Purpose:
The Node class is used by the tree data structure

Object Variables:
    parent (parent node)
    children (list of child nodes)
    heuristic (heuristic value of node)
    depth (depth of node in tree)
    board (board object to be analyzed at current node)
    index (the touched tile to create current node)

Constructor takes in the above-mentioned variables
"""


class Node:
    def __init__(self, parent, children, heuristic, depth, board, index):
        self.parent = parent
        self.children = children
        self.heuristic = heuristic
        self.depth = depth
        self.board = board
        self.index = index
