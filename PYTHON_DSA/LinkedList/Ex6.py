# Reverse a Linked List

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

# Reverse Iterative:
def print_list(head):
    curr = head

    while curr is not None:
        print(curr.data, end="➡ ")
        curr = curr.next

    print("None")


def reverse(head):
    prev = None
    nxt = None
    curr = head

    while curr != None:

        nxt = curr.next
        curr.next = prev

        prev = curr
        curr = nxt

    return prev

print("Original list:")
print_list(head)

head = reverse(head) #function call ke baad head change ho gaya.
print("Reversed list:")
print_list(head)



# Reverse Recursively:
def reverse_2(head):

    if head == None or head.next == None:
        return head
    
    new_head = reverse_2(head.next) #recursive call

    head.next.next = head
    head.next = None

    return new_head

print("Original list:")
print_list(head)

head = reverse_2(head)  #function call ke baad head change ho gaya.
print("Recursively reversed:")
print_list(head)