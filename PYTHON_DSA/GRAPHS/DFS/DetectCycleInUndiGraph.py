## Detect Cycle in Undirected Graph

def dfs(node, parent):
    visited[node] = True

    for neighbour in graph[node]:
        if not visited[neighbour]:
            if dfs(neighbour, node):
                return True
            
            elif neighbour != parent:
                return True
            
    return False

graph = [
    [1,2],
    [0,2],
    [0,1]
]

visited = [False] * len(graph)

print(dfs(0,-1))
