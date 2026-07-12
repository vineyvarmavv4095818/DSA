## Find path between two nodes

from collections import deque

def bsf(start, target, graph, visited):
    q = deque([start])
    visited[start] = True

    path_found = False

    while q:
        node = q.popleft()
        if node == target:
            path_found = True
            break

        for neighbour in graph[node]:
            if not visited[neighbour]:
                visited[neighbour] = True
                q.append(neighbour)

    return path_found

graph = [
    [1,2],
    [0],
    [0,3],
    [2],
    [5],
    [4]
]

visited = [False] * len(graph)

print(bsf(0,1, graph, visited))