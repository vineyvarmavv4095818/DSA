# Find Intersaction Of Two Sorted Lists

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head1 = Node(1)
head1.next = Node(3)
head1.next.next = Node(4)
head1.next.next.next = Node(10)

head2 = Node(2)
head2.next = Node(2)
head2.next.next = Node(4)
head2.next.next.next = Node(10)

def intersection(head1, head2):
    temp1 = head1
    temp2 = head2

    l1 = 0
    while temp1 != None:
        l1 += 1
        temp1 = temp1.next

    l2 = 0
    while temp2 != None:
        l2 += 1
        temp2 = temp2.next

    temp1 = head1
    temp2 = head2

    if l1 > l2:
        steps = l1 - l2
        for i in range(steps):
            temp1 = temp1.next

    else:
        steps = l2 - l1
        for i in range(steps):
            temp2 = temp2.next

    while temp1.data != temp2.data:
        temp1 = temp1.next
        temp2 = temp2.next

    return temp1.data

print(intersection(head1, head2))