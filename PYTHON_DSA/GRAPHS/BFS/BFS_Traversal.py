from collections import deque

def bfs(node, graph, visited):
    q = deque([node])
    # q.append(node)
    visited[node] = True

    while q:
        e = q.popleft()
        print(e, end=" ")

        for neighbour in graph[e]:
            if not visited[neighbour]:
                visited[neighbour] = True
                q.append(neighbour)

graph = [
    [2,8],
    [1,3,4],
    [2],
    [2,5],
    [4,6],
    [5,7],
    [6,8],
    [1,7],
    [8],
]

visited = [False] * len(graph)
bfs(1, graph, visited)