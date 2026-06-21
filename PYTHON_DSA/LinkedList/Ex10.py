# Check Palindrome Linked List


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

a = Node(10)
b = Node(20)
c = Node(30)
d = Node(20)
e = Node(10)

a.next = b
b.next = c
c.next = d
d.next = e

head = a

def is_palindrome(head):

    arr = []

    curr = head

    while curr != None:

        arr.append(curr.data)
        curr = curr.next

    return arr == arr[::-1]  #[start:End:step]

print(is_palindrome(head))