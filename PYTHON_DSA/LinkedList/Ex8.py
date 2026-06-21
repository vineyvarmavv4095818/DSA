# Length of Loop

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
e.next = d #loop bna diya

head = a

def length(head):

    slow = head
    fast = head

    while fast != None and fast.next != None:

        slow = slow.next
        fast = fast.next.next

        if slow == fast:

            count = 1
            slow = slow.next

            while slow != fast:

                slow = slow.next
                count += 1

            return count

    return None

print(length(head))