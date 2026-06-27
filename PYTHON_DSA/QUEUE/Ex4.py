## Reverse Queue using Stack

from collections import deque

q = deque([1,2,3,4])

st = []
print("Before reverse:",q)
while q:
    st.append(q.popleft())

while st:
    q.append(st.pop())

print("After reverse:",q)