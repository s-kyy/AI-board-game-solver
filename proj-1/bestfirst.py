from Tree import Tree
from Node import Node
from setup import atGoal
from board import heuristicValue, heuristicOption
import os
"""
Project 1.1: Best First Search Algorithm
COMP 472 NN
DUE: Feb 9th, 2020
Samantha Yuen (40033121), Andrew Marcos (40011252), Michael Gagnon (40030481)

Purpose:
The BestFirstSearch class is responsible for running the Best First Search search on the board object

Open list = list (priority queue behaviour)
closed list = dictionary
Tree Data structure -- From the root/parent, we can have nxn different children
depth-level should start at 1

Object Methods:
    startSearch(self, tree) -- Starts the best first search search on tree
    finish(self, node, found) -- Ends the search by finding solution path and write to solution path if found.
    generateChildren(self, node) -- Generates children of node.
    bestFirstSearch(self, board) -- Initializes the search by create tree and root and starts the best first search
    createTouchOptions(self, board) -- Creates all of the possible tile options of the given board
"""


class BestFirstSearch:
    def __init__(self):
        self.counter = 0

    def startSearch(self, tree):
        searchFileName = os.getcwd() + '/output/' + \
            str(tree.head.board.num) + '_bfs_search.txt'
        os.makedirs(os.path.dirname(searchFileName), exist_ok=True)
        with open(searchFileName, 'w') as search:
            # Keep searching until open list is empty or we reach max length path
            while(len(tree.openlist) != 0 and self.counter < tree.head.board.maxL):
                currentNode = tree.openlist.pop(0)
                # If we've seen this node before, skip it
                if(currentNode.board.printState() not in tree.closedlist):
                    search.write(
                        '0 0 ' + str(currentNode.h) + ' ' + currentNode.board.printState() + '\n')
                    if(atGoal(currentNode.board.state)):
                        return self.finish(currentNode)
                    tree.closedlist[currentNode.board.printState()] = True
                    # print('length of closed list: ' + str(len(tree.closedlist)))

                    listOfChildren = self.generateChildren(
                        currentNode)
                    # print(len(listOfChildren))
                    currentNode.children = listOfChildren
                    for child in listOfChildren:
                        if(child.board.printState() not in tree.closedlist):
                            tree.openlist.append(child)
                tree.openlist.sort(key=lambda x: (
                    x.f, x.board.printState()))

            self.finish(tree.head, False)

    def finish(self, node, found=True):
        solutionFileName = os.getcwd()+'/output/' + \
            str(node.board.num)+'_bfs_solution.txt'
        os.makedirs(os.path.dirname(solutionFileName), exist_ok=True)
        if(found):
            completedPath = [node]
            # Keep looping until we get to the head of the tree.
            while(node.parent is not None):
                node = node.parent
                completedPath.append(node)
            with open(solutionFileName, 'w') as solution:
                # loop in the reverse direction
                for node in reversed(completedPath):
                    solution.write(node.index + ' ' +
                                   node.board.printState() + '\n')
        else:
            with open(solutionFileName, 'w') as solution:
                solution.write('no solution')
        return True

    def generateChildren(self, node):
        listOfChildsNodes = []
        # x in this case is the index of the board that I want to call
        # touch() on.
        for x in self.touchOptions:
            newBoard = node.board.touch(x)
            h = heuristicValue(newBoard, heuristicOption)
            childNode = Node(node, [], h, node.depth + 1, newBoard, x, h)
            listOfChildsNodes.append(childNode)
        return listOfChildsNodes

    def bestFirstSearch(self, board):
        # Node(Parent Node, List of children nodes, heuristic value, depth value, board object, index, totalHeuristic)
        h = heuristicValue(board, heuristicOption)
        # Since BFS doesnt care about the position in the search space, total f = h
        head = Node(None, [], h, 1, board, "0", h)
        tree = Tree(head)
        self.touchOptions = self.createTouchOptions(board)
        tree.openlist.append(head)

        return self.startSearch(tree)

    def createTouchOptions(self, board):
        counterLetter = 0
        choices = []
        while counterLetter < board.size:
            # chr(65) = A
            chrIndex = 65 + counterLetter
            counterNumber = 1
            while counterNumber < board.size+1:
                choices.append(chr(chrIndex) + ''+str(counterNumber))
                counterNumber += 1
            counterLetter += 1

        return choices
