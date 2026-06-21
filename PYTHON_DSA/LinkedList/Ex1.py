class Node:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def Solution(head):
    curr = head
    l = 0

    while curr != None:
        curr = curr.next
        l += 1

    curr = head
    for i in range(l//2):
        curr = curr.next

    return curr


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.next = b
b.next = c
c.next = d
d.next = e

head = a
print(Solution(head).data)