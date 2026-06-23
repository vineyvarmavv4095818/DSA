# Remove Duplicates from Sorted List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

a = Node(10)
b = Node(20)
c = Node(30)
d = Node(30)
e = Node(50)

a.next = b
b.next = c
c.next = d
d.next = e

head = a

def printList(head):
    curr = head
    while curr:
        print(curr.data, end="➡ ")
        curr = curr.next

    print("None")


def remove_dulpicate(head):

    curr = head

    while curr and curr.next:

        if curr.data == curr.next.data:
            curr.next = curr.next.next

        else:
            curr = curr.next

    return head

new_head = remove_dulpicate(head)
printList(new_head)