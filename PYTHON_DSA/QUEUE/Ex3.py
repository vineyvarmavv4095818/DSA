## Generate Binary Numbers from 1 to N

from collections import deque

def bianry(n):

    q = deque()

    q.append("1")

    for i in range(n):

        s = q.popleft()

        print(s)

        q.append(s+"0")
        q.append(s+"1")


bianry(5)