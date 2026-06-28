## Reverse First K Elements

from collections import deque

q = deque([1,2,3,4,5])

st = []
k = 3

for i in range(k):
    st.append(q.popleft())

while st:
    q.append(st.pop())

for i in range(len(q)-k):
    q.append(q.popleft())

print(q)