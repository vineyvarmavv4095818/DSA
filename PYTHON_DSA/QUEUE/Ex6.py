## Implement Stack using Queue

from collections import deque

class Stack:
    def __init__(self):
        self.q = deque()

    def push(self, x):

        self.q.append(x)

        for i in range(len(self.q)-1):
            self.q.append(self.q.popleft())

    def pop(self):
        return self.q.popleft()
    
    def top(self):
        print(self.q[0])

    def empty(self):
        return len(self.q) == 0



s = Stack()

# s.push(10)
# s.push(20)
# s.push(30)

print(s.empty())