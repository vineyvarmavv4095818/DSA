## Shortest Path in Unweighted Graph

from collections import deque

def bfs(start):
    q = deque([start])
    distance[start] = 0

    while q:
        node = q.popleft()

        for neighbour in graph[node]:
            if distance[neighbour] == -1:
                distance[neighbour] = distance[node] + 1
                q.append(neighbour)

    return distance

graph = [
    [1,2],
    [0,3],
    [0,3],
    [1,2]
]

distance = [-1] * len(graph)

print(bfs(0))