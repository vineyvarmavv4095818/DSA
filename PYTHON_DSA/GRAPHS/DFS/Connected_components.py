## Check connected components

def dfs(node, graph, visited):
    visited[node] = True

    for neighbour in graph[node]:
        if not visited[neighbour]:
            dfs(neighbour, graph, visited)

graph = [
    [1],
    [0],
    [3],
    [2],
    [5],
    [4],
    []
]

visited = [False] * len(graph)
connected = 0

for i in range(len(graph)):
    if not visited[i]:
        dfs(i, graph, visited)
        connected += 1

print(connected)