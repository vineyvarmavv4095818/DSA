class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

a = Node(4)
b = Node(6)
c = Node(10)

a.next = b
b.next = c

head = a   # start node a ko head bnaya

def PrintLinkedList(head):  # linked list me traverse krne or print krane ke liye function

    curr = head
    while curr != None:
        print(curr.data, end=" ")
        curr = curr.next


# add node at beginning

NewNode = Node(3)  # create a new node

NewNode.next = head  # new node ko head se connect kiya
head = NewNode      # head ko beginning me le aaye

# add node at end

NewNode = Node(1)  # create a new node

curr = head  # head ko curr me dalo
while curr.next != None:  # curr ko end me phuchao
    curr = curr.next

curr.next = NewNode  # ab curr end me aane ke bad usme new node add krdo

# add node at the kth index

k = 2  # jis index pr insert krna hai
NewNode = Node(5)

curr = head  # head ko firse curr pr lao
for i in range(k-1):
    curr = curr.next   # k pr add krne ke liye usse pehle wale node tk jao

NewNode.next = curr.next   # ab jo curr ka next hai use new node ke next me daal do (pehle baad wale node ke just pehle ad kro)
curr.next = NewNode # ab jo new node hai use curr ke next me daal do (fir jo pehle wala node hai uske just baad add kro)


# Deleting the first node

head = head.next

# Deleting the last node

curr = head
while curr.next.next != None:
    curr = curr.next

curr.next = None

# Deleting kth node

k = 2
curr = head
for i in range(k-1):
    curr = curr.next

curr.next = curr.next.next  # k = 2 node ko delete krke uske agle node ko curr ka next bnaya
PrintLinkedList(head)