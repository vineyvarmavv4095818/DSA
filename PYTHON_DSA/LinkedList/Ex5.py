# Find Middle Node


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

a = Node(10)
b = Node(20)
c = Node(30)
d = Node(40)
e = Node(50)
f = Node(60)
g = Node(70)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g

head = a

# Brute force:
def find_mid(head):

    l = 0
    curr = head
    while curr != None:
        l += 1
        curr = curr.next

    curr = head
    for i in range(l//2):
        curr = curr.next

    return curr.data

print(find_mid(head))


#Optimal(Slow Fast):
def middle(head):

    slow = head
    fast = head
    
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next

    return slow.data

print(middle(head))