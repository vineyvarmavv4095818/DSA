# Merge two sorted Linked lists

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head1 = Node(1)
head1.next = Node(3)
head1.next.next = Node(5)

head2 = Node(2)
head2.next = Node(4)
head2.next.next = Node(6)

def printList(head):
    curr = head

    while curr:
        print(curr.data, end="➡ ")
        curr = curr.next

    print("None")

def merge(head1, head2):

    if head1==None or head2==None:
        return head2 if head1==None else head1

    if head1.data <= head2.data:
        head1.next = merge(head1.next, head2)
        return head1

    else: head2.next = merge(head1, head2.next)
    return head2

merged_head = merge(head1, head2)  # yaha merged_head final merged list ka head hai.
printList(merged_head)

