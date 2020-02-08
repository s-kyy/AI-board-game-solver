class Tree:
    def __init__(self, head):
        self.head = head
        self.openlist = []
        self.closedlist = {}
