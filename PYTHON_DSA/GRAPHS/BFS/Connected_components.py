from collections import deque

def bfs(start):
    q = deque([start])
    visited[start] = True

    while q:
        node = q.popleft()

        for neighbour in graph[node]:
            if not visited[neighbour]:
                visited[neighbour] = True
                q.append(neighbour)

graph = [
    [1],
    [0,2],
    [1],
    [4],
    [3],
    [6,7],
    [5],
    [5]
]

visited = [False] * len(graph)
component = 0

for i in range(len(graph)):
    if not visited[i]:
        bfs(i)
        component += 1

print(component)