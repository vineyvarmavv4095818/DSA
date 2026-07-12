# def dfs(node, ans, visited, adj):
#     visited[node] = 1
#     ans.append(node)

#     for n in adj[node]:
#         if visited[n] == 0:
#             dfs(n, ans, visited, adj)

# number_of_nodes = 8
# adj = [[],[2,4],[1,3,6],[2],[1,5,7],[4,8],[2],[4,8],[5,7]]
# visited = [0] * (number_of_nodes + 1)
# ans = []
# dfs(1, ans, visited, adj)
# print(ans)

## Answer without array

def dfs(node, graph, visited):
    visited[node] = True
    print(node, end=" ")

    for neighbour in graph[node]:
        if not visited[neighbour]:
            dfs(neighbour,graph, visited)

graph = [
    [1,2],
    [0,3],
    [0,3],
    [1,2]
]

visited = [False] * len(graph)

dfs(0, graph, visited)