## Shortest Path in Unweighted Graph (BFS)

from collections import deque

graph = [
    [1,2],
    [0,3],
    [0,3],
    [1,2]
]
distance = [-1] * 4
queue = deque([0])
distance[0] = 0

while queue:
    node = queue.popleft()
    for neighbour in graph[node]:
        if distance[neighbour] == -1:
            distance[neighbour] = distance[node] + 1
            queue.append(neighbour)
print(distance)