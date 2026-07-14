## Detect cycle in directed graph

def dfs(node):
    visited[node] = True
    pathVisited[node] = True

    for neighbour in graph[node]:
        if not visited[neighbour]:
            if dfs(neighbour):
                return True
            
        elif pathVisited[neighbour]:
            return True
        
    pathVisited[node] = False
    return False

graph = [
    [1],
    [2],
    [3],
    []
]

visited = [False] * len(graph)
pathVisited = [False] * len(graph)

print(dfs(0))