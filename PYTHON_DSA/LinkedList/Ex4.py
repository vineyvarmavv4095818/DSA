class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

a = Node(10)
b = Node(20)
c = Node(30)
d = Node(40)

a.next = b
b.next = c
c.next = d

head = a

def traverse(head):
    curr = head

    while curr != None:
        print(curr.data, end=" ")
        curr = curr.next

new = Node(0)
new.next = head
head = new

# traverse(head)

new = Node(50)
curr = head
while curr.next != None:
    curr = curr.next

curr.next = new

# traverse(head)

k = 3
new = Node(25)

curr = head
for i in range(k-1):
    curr = curr.next

new.next = curr.next
curr.next = new

# traverse(head)

head = head.next

# traverse(head)

curr = head
while curr.next.next != None:
    curr = curr.next

curr.next = None

# traverse(head)

val = 25

if head.data == val:
    head = head.next

curr = head
while curr.next != None:

    if curr.next.data == val:
        curr.next = curr.next.next
        break

    curr = curr.next

traverse(head)


