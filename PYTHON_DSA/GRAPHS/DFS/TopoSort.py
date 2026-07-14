## Topological Sort by DFS

def topo_sort(graph):
    visited = set()
    stack = []

    def dfs(node):
        visited.add(node)

        for neighbour in graph[node]:
            if neighbour not in visited:
                dfs(neighbour)

        stack.append(node)

    for i in graph:
        if i not in visited:
            dfs(i)
    
    return stack[::-1]

graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': ['E'],
    'E': []
}

print(topo_sort(graph))