class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.que = [None]*size
        self.front = self.rear = -1

    def enqueue(self, x):
        if self.isFull():
            print("Queue is full.")
        elif self.front == -1:
            self.front = self.rear = 0
            self.que[self.rear] = x
        else:
            self.rear = (self.rear+1)%self.size
            self.que[self.rear] = x

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty.")
        elif self.front == self.rear:
            print(self.que[self.front])
            self.front = self.rear = -1
        else:
            print(self.que[self.front])
            self.front = (self.rear+1)%self.size

    def isEmpty(self):
        return self.front == -1
    
    def isFull(self):
        return ((self.rear+1) % self.size == self.front)
    
    def Size(self):
        print(self.size)


cq = CircularQueue(6)

cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.enqueue(50)
cq.enqueue(60)

cq.dequeue()
cq.Size()
