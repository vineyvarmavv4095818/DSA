def dfs(node, graph, color):
    
    for neighbour in graph[node]:

        if color[neighbour] == -1:
            color[neighbour] = 1 - color[node]

            if not dfs(neighbour, graph, color):
                return False
            
        elif color[neighbour] == color[node]:
            return False
        
    return True

def is_bipartite(graph):

    color = [-1] * len(graph)

    for i in range(len(graph)):

        if color[i] == -1:
            color[i] = 0

            if not dfs(i, graph, color):
                return False
    return True

graph = [
    [1,2],
    [0],
    [0]
]

print(is_bipartite(graph))

