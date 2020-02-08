from Tree import Tree
from Node import Node
from setup import atGoal
import os
"""
Project 1.1: Depth First Search Algorithm
COMP 472 NN 
DUE: Feb 9th, 2020
Samantha Yuen (40033121), Andrew Marcos (40011252), Michael Gagnon (40030481)

Purpose:
The DFS class is responsible for running the DFS search on the board object

Open list = stack (list)
closed list = dictionary
Tree Data structure -- From the root/parent, we can have nxn different children 
depth-level should start at 0 or 1

Object Methods:
    startSearch(self, tree) -- Starts the DFS search on tree
    finish(self, node, found) -- Ends the search by finding solution path and write to solution path if found.
    generateChildren(self, node, sortChilds) -- Generates children of node with the tie-breaker sort.
    dfsSearch(self, board) -- Initializes the search by create tree and root and starts the dfs search
    createTouchOptions(self, board) -- Creates all of the possible tile options of the given board
"""


class DFS:
    def __init__(self):
        pass

    def startSearch(self, tree):
        searchFileName = os.getcwd() + '/output/' + \
            str(tree.head.board.num) + '_dfs_search.txt'
        os.makedirs(os.path.dirname(searchFileName), exist_ok=True)
        with open(searchFileName, 'w') as search:
            while(len(tree.openlist) != 0):
                currentNode = tree.openlist.pop()
                #print("--- Analyzed node ---")
                # print(currentNode.board.printState())
                #print("--- Analyzed node ---")
                # If we've seen this node before, skip it
                if(currentNode.board.printState() not in tree.closedlist):
                    search.write(
                        '0 0 0 ' + currentNode.board.printState() + '\n')
                    if(atGoal(currentNode.board.state)):
                        return self.finish(currentNode)
                    tree.closedlist[currentNode.board.printState()] = True
                    # print('length of closed list: ' + str(len(tree.closedlist)))

                    # Do not create children for nodes at max depth
                    if(currentNode.board.maxD != currentNode.depth):
                        listOfChildren = self.generateChildren(
                            currentNode)
                        # print(len(listOfChildren))
                        currentNode.children = listOfChildren
                        for child in reversed(listOfChildren):
                            if(child.board.printState() not in tree.closedlist):
                                tree.openlist.append(child)

                    #input('enter to continue')
                    # print('length of openlist: '+str(len(tree.openlist)))
            self.finish(tree.head, False)

    def finish(self, node, found=True):
        solutionFileName = os.getcwd()+'/output/' + \
            str(node.board.num)+'_dfs_solution.txt'
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

    def generateChildren(self, node, sortChilds=True):
        childNodes = {}
        listOfChildsNodes = []
        # x in this case is the index of the board that I want to call
        # touch() on.
        if(sortChilds):
            for x in self.touchOptions:
                newBoard = node.board.touch(x)
                childNode = Node(node, [], 0, node.depth + 1, newBoard, x)
                childNodes[childNode.board.printState()] = childNode
            '''
            This tie-breaker sort is kind of 'cheating' for DFS. It is providing it
            some sort of heuristic ordering since the
            state with the most amount of leading zeros is very likely
            to be the state that is closest to being solved. I have provided
            two paths, one without the tie breakers and one with. By disabling
            the tie breaker the DFS search takes much much longer since it's truly
            doing a brute search across all nodes. Depending on the size of the puzzle,
            this can result in a of search 2^100 = a 302 digit number of states.
            '''
            sorted_childNodes = dict(sorted(childNodes.items()))
            print('----')
            for key, value in sorted_childNodes.items():
                print(value.board.printState())
                listOfChildsNodes.append(value)
        else:
            for x in self.touchOptions:
                newBoard = node.board.touch(x)
                childNode = Node(node, [], 0, node.depth + 1, newBoard, x)
                listOfChildsNodes.append(childNode)

        return listOfChildsNodes

    def dfsSearch(self, board):
        # Node(Parent Node, List of children nodes, heuristic value, depth value, board object)
        # The first Node does not have a parent, no children for now, DFS does not have a heuristic,
        # a depth of 1, the initial state of the board and an empty move.
        head = Node(None, [], 0, 1, board, "0")
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
