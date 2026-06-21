class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

a = Node(10)
b = Node(20)
c = Node(30)

a.next = b
b.next = c

head = a

def traverse(head):

    c = 0

    curr = head
    while curr != None:
        print(curr.data, end=" ")
        c += 1
        curr = curr.next
    print("\n")
    print("Number of nodes:",c)

traverse(head)