## Interleave First Half and Second Half Queue

from collections import deque

q = deque([1,2,3,4])

stack = []

for i in range(len(q)//2):
    stack.append(q.popleft())

result = deque()

while stack:
    result.append(stack.pop())
    result.append(q.popleft())

print(result)