## Array(List) implementaton of Stack:

class Stack:
    def __init__(self):
        self.st = []

    def push(self, x):
        self.st.append(x)
        return


    def pop(self):
        if len(self.st) == 0:
            return None
        x = self.st[-1]
        self.st.pop()
        return x

    def top(self):
        if len(self.st) == 0:
            return None
        return self.st[-1]

    def size(self):
        return len(self.st)


## Linked List implementaton of Stack:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.length = 0

    def push(self, x):
        self.length += 1

        if self.top is None:
            self.top = Node(x)
            return

        newNode = Node(x)
        newNode.next = self.top
        self.top = newNode

    def pop(self):
        self.length -= 1
        if self.top is None:
            return -1
        

        x = self.top.data
        self.top = self.top.next
        return x

    def getTop(self):
        if self.top is None:
            return -1
        else:
            return self.top.data

    def size(self):
        return self.length
    
    def isEmpty(self):
        if self.length is 0:
            return True
        return False


## 3rd way

class Stack:

    def __init__(self):
        self.st = []

    def push(self, x):
        self.st.append(x)
        print("item",x, "added.")

    def pop(self):
        if self.is_empty():
            return None
        return print("item",self.st.pop(),"is removed.")

    def peek(self):
        if self.is_empty():
            return None
        return print("top of stack is:", self.st[-1])

    def is_empty(self):
        return len(self.st) == 0

    def size(self):
        return print("Length of stack:", len(self.st))
    
    def display(self):
        print(self.st)