class Node:
    def __init__(self, parent, children, heuristic, depth, board, index):
        self.parent = parent
        self.children = children
        self.heuristic = heuristic
        self.depth = depth
        self.board = board
        self.index = index
