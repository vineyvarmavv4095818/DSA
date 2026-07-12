## BFS Level Order Traversal

from collections import deque

graph = [
    [1,2],
    [0,3,4],
    [0],
    [1],
    [1]
]

visited = [False] * len(graph)
q = deque([0])
visited[0] = True
level = 0

while q:

    size = len(q)
    print("Level",level,":")

    for _ in range(size):
        node = q.popleft()
        print(node, end=" ")

        for neighbour in graph[node]:
            if not visited[neighbour]:
                visited[neighbour] = True
                q.append(neighbour)

    print()
    level += 1