## Detect Cycle in Undirected Graph

from collections import deque

def bfs(node, parent):

    q = deque([(node,parent)])
    visited[node] = True

    cycle = False

    while q:
        n, p = q.popleft()

        for neighbour in graph[n]:
            if not visited[neighbour]:
                visited[neighbour] = True
                q.append((neighbour,n))

            elif neighbour != n:
                cycle = True

    return cycle

graph = [
    [1,2],
    [0,2],
    [0,1]
]

visited = [False] * len(graph)

print(bfs(0, -1))

