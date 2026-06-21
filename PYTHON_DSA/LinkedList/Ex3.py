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

def search(head, tar):

    curr = head

    while curr != None:

        if(curr.data == tar):
            return True

        curr = curr.next

    return False

print(search(head, 50))