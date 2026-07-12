## Count reachable nodes
from collections import deque

def bfs(node, graph, visited):
    q = deque([node])
    visited[node] = True

    count = 0

    while q:
        e = q.popleft()
        count += 1

        for neighbour in graph[e]:
            if not visited[neighbour]:
                visited[neighbour] = True
                q.append(neighbour)

    return count

graph = [
    [1,2],
    [0],
    [0,3],
    [2],
    []
]

visited = [False] * len(graph)
print(bfs(0, graph, visited))