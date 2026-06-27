class Deque:
    def __init__(self):
        self.dq = []

    def insertAtFront(self, x):
        self.dq.insert(0, x)

    def deleteFromEnd(self):
        if len(self.dq)==0:
            return 0
        else:
            self.dq.pop()

    def insertAtEnd(self, x):
        self.dq.append(x)

    def deleteFromFront(self):
        if len(self.dq)==0:
            return 0
        else:
            self.dq.pop(0)

    def display(self):
        return self.dq

