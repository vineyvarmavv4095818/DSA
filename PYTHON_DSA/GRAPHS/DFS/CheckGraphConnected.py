## Check graph connected

def dfs(node, graph, visited):
    visited[node] = True

    for neighbour in graph[node]:
        if not visited[neighbour]:
            dfs(neighbour, graph, visited)

graph = [
    [1,2],
    [0],
    [0,3],
    [2]
]

visited = [False] * len(graph)

dfs(0, graph, visited)

print(all(visited))