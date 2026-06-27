class Queue:
    def __init__(self):
        self.que = []
    
    def isEmpty(self):
        return len(self.que)==0
    
    def insert(self, x):
        self.que.append(x)

    def delete(self):
        if len(self.que)==0:
            return 0
        else:
            return self.que.pop(0)
    
    def display(self):
        return self.que
        
q = Queue()

q.insert(2)
q.insert(3)
q.insert(1)
q.insert(4)

print(q.display())
print(q.delete())
print(q.display())
q.insert(6)
print(q.display())
print(q.isEmpty())
