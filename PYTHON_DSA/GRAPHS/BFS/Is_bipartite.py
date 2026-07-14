## Is Graph Bipartite (BFS)

from collections import deque

def isBipartite(graph, color):

    for start in range(len(graph)):
        if color[start] != -1:
            continue

        q = deque([start])
        color[start] = 0

        while q:
            node = q.popleft()

            for neighbour in graph[node]:

                if color[neighbour] == -1:
                    color[neighbour] = 1 - color[node]
                    q.append(neighbour)

                elif color[neighbour] == color[node]:
                    return False
    
    return True

graph = [
    [1,2],
    [0,2],
    [0,1]
]

color = [-1] * len(graph)
print(isBipartite(graph, color))