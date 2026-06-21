# Find nth node from end

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

a = Node(10)
b = Node(20)
c = Node(30)
d = Node(40)
e = Node(50)

a.next = b
b.next = c
c.next = d
d.next = e

head = a

def find(head, n):

    first = head
    second = head

    for i in range(n):
        first = first.next

    while first != None:

        first = first.next
        second = second.next

    return second.data

print(find(head, 5))