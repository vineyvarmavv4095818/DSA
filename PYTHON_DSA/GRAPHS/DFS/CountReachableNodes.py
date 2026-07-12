## Count reachable nodes

def dfs(node, graph, visited):
    visited[node] = True
    count = 1

    for neighbour in graph[node]:
        if not visited[neighbour]:
            count += dfs(neighbour, graph, visited)

    return count

graph = [
    [1,2],
    [0],
    [0,3,5],
    [2,4],
    [3],
    [2]
]

visited = [False] * len(graph)
print(dfs(0, graph, visited))