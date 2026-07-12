## Find path between two nodes

def dfs(node, target, graph, visited):
    if node == target:
        return True
    
    visited[node] = True

    for neighbour in graph[node]:
        if not visited[neighbour]:
            if dfs(neighbour, target, graph, visited):
                return True
            
    return False

graph = [
    [1,2],
    [0],
    [0,3],
    [2],
    [5],
    [4]
]

visited = [False] * len(graph)

print(dfs(0,1, graph, visited))

