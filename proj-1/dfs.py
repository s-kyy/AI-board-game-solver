from Tree import Tree
from Node import Node

"""
Project 1.1: Depth First Search Algorithm
COMP 472 NN 
DUE: Feb 9th, 2020
Samantha Yuen (40033121), Andrew Marcos (40011252), Michael Gagnon (40030481)

Open list = stack
Tree Data structure -- From the root/parent, we can have nxn different children 
depth-level should start at 0 or 1
Must output dfs.solution.txt and dfs.search.txt files 
"""

def startSearch(tree, node):
    searchFileName = node.state.num + '_dfs_search.txt'
    with open(searchFileName, 'a') as search:
        search.write('0 0 0 ' + node.state.output())

    if(node.state.isGoalState()):
        return finish(node)
    tree.closedlist.append(node.state)

    listOfChildren = generateChildren(node)
    node.children = listOfChildren
    for child in reversed(listOfChildren):
        if(child.state not in tree.closedlist and child.state not in tree.openlist):
            tree.openlist.append(child)


    startSearch(tree, tree.openlist[-1])


def finish(node):
    completedPath = [node]
    # Keep looping until we get to the head of the tree.
    while(node.Parent is not None):
        node = node.Parent
        completedPath.append(node)
    
    # write the completed path to the solution file
    solutionFileName = node.state.num+'_dfs_solution.txt'
    with open(solutionFileName, 'a') as solution:
        # loop in the reverse direction
        for node in reversed(completedPath):
            solution.write(node.index + ' ' + node.state.output())
    

def generateChildren(node):
    childNodes = []
    # x in this case is the index of the board that I want to call
    # touch() on.
    for x in node.state:
        newBoard = node.state.touch(x)
        childNode = Node(node, [], 0, node.depth + 1, newBoard, x)
        childNodes.append(childNode)
    # TODO: Sort this childNodes array
    return childNodes
    

def dfsSearch(board):
    # Node(Parent Node, List of children nodes, heuristic value, depth value, board object)
    # The first Node does not have a parent, no children for now, DFS does not have a heuristic,
    # a depth of 1, the initial state of the board and an empty move.
    head = Node(None, [], 0, 1, board, "0")
    tree = Tree(head)

    return startSearch(tree, head)






