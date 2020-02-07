class Tree:
    def __init__(self, head):
        self.head = head
        self.openlist = []
        self.closedlist = {}

    def printTree(self):
        print(self.head.state)
        for x in self.head.children:
            x.printChildren()
