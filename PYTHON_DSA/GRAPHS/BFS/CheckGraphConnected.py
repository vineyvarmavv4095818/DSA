## Check graph connected

from collections import deque

def bfs(start, graph, visited):
    q = deque([start])
    visited[start] = True

    while q:
        node = q.popleft()

        for neighbour in graph[node]:
            if not visited[neighbour]:
                visited[neighbour] = True
                q.append(neighbour)

    return all(visited)

graph = [
    [1],
    [0],
    [3],
    [2],
]

visited = [False] * len(graph)

print(bfs(0, graph, visited))