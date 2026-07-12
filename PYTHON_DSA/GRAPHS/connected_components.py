## Counr connected components
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
]

visited = [False]*5

count = 0

for i in range(len(graph)):
    if not visited[i]:
        dfs(i, graph, visited)
        count +=1

print(count)

## Leetcode

# class Solution(object):
#     def dfs(self, node, isConnected, visited):

#         visited[node] = True
        
#         for neighbour in range(len(isConnected)):
#             if isConnected[node][neighbour] == 1 and not visited[neighbour]:
#                 self.dfs(neighbour, isConnected, visited)

#     def findCircleNum(self, isConnected):
#         n = len(isConnected)
#         visited = [False]*n

#         count = 0

#         for i in range(n):
#             if not visited[i]:
#                 self.dfs(i, isConnected, visited)
#                 count +=1

#         return count