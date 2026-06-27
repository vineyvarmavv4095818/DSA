## Array(List) implementaton of Queue:

class Queue:
    def __init__(self):
        self.q = []
        self.front = -1

    def push(self, x):
        if self.front == -1:
            self.front = 0
        self.q.append(x)
        return


    def pop(self):
        if len(self.q) == 0:
            return -1
        x = self.q[self.front]
        self.front += 1
        if self.front == len(self.q):
            self.front = -1
            self.q = []
        return x

    def getFront(self):
        if len(self.q) == 0:
            return -1
        return self.q[self.front]

    def size(self):
        if self.front == -1:
            return 0
        return len(self.q) - self.front





## Linked List implementaton of Queue:

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0

    def push(self, x):
        self.length += 1
        newNode = Node(x)
        if self.front == None:
            self.front = newNode
            self.rear = newNode
        else:
            self.rear.next = newNode
            self.rear = newNode

    def pop(self):
        self.length -= 1
        if self.front == None:
            return -1
        
        x = self.front.data
        self.front = self.front.next
        if self.front == None:
            self.rear = None
        return x
    
    def getFront(self):
        if self.front == None:
            return -1
        return self.front.data

    def size(self):
        if self.front == None:
            return 0
        return self.length




