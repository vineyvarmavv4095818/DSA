## Valid graph tree

def dfs(node, parent):
    visited[node] = True

    for neighbour in graph[node]:
        if not visited[neighbour]:
            if dfs(neighbour, node):
                return True
            
        elif neighbour != parent:
            return True
        
    return False

graph=[
    [1],
    [0,2],
    [1]
]

visited = [False] * len(graph)

cycle = dfs(0,-1)

connected = all(visited)

print((not cycle) and connected)