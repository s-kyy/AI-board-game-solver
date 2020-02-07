from Tree import Tree
from Node import Node
from setup import atGoal

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


class DFS:
    def __init__(self):
        pass

    def startSearch(self, tree):
        searchFileName = str(tree.head.board.num) + '_dfs_search.txt'
        with open(searchFileName, 'w') as search:
            while(len(tree.openlist) != 0):
                currentNode = tree.openlist.pop()
                search.write('0 0 0 ' + currentNode.board.printState() + '\n')
                if(atGoal(currentNode.board.state)):
                    return self.finish(currentNode)
                tree.closedlist[currentNode.board.printState()] = True
                print('length of closed list: ' + str(len(tree.closedlist)))

                # Do not create children for nodes at max depth
                if(currentNode.board.maxD != currentNode.depth):
                    listOfChildren = self.generateChildren(currentNode)
                    # print(len(listOfChildren))
                    currentNode.children = listOfChildren
                    for child in reversed(listOfChildren):
                        if(child.board.printState() not in tree.closedlist):
                            tree.openlist.append(child)

                #input('enter to continue')
                print('length of openlist: '+str(len(tree.openlist)))
            print(tree.closedlist)
            print('no solution')
            self.finish(tree.head, False)

    def finish(self, node, found=True):
        solutionFileName = str(node.board.num)+'_dfs_solution.txt'
        if(found):
            completedPath = [node]
            # Keep looping until we get to the head of the tree.
            while(node.parent is not None):
                node = node.parent
                completedPath.append(node)

            # write the completed path to the solution file
            solutionFileName = str(node.board.num)+'_dfs_solution.txt'
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
        childNodes = []
        # x in this case is the index of the board that I want to call
        # touch() on.
        for x in self.touchOptions:
            # print(x)
            newBoard = node.board.touch(x)
            # print(newBoard.printState())
            childNode = Node(node, [], 0, node.depth + 1, newBoard, x)
            childNodes.append(childNode)
        # TODO: Sort this childNodes array
        return childNodes

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
        print(board.size)
        while counterLetter < board.size:
            # chr(65) = A
            chrIndex = 65 + counterLetter
            counterNumber = 1
            while counterNumber < board.size+1:
                choices.append(chr(chrIndex) + ''+str(counterNumber))
                counterNumber += 1
            counterLetter += 1

        print(choices)
        return choices
