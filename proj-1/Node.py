class Node:
    def __init__(self, parent, children, heuristic, depth, state, index):
        self.parent = parent
        self.children = children
        self.heuristic = heuristic
        self.depth = depth
        self.state = state
        self.index = index
    
    def printChildren(self):
        print(self.state)
        for x in self.children:
            x.printChildren()