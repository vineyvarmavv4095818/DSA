from collections import deque

def bfs(n, adj, starting_node):

    ans = []
    queue = deque()
    visited = [0] * (n+1)

    queue.append(starting_node)
    visited[starting_node] = 1

    while queue:

        e = queue.popleft()
        ans.append(e)

        for node in adj[e]:
            if visited[node] == 0:
                queue.append(node)
                visited[node] = 1

    return ans

n = 8

adjacency_list = [
    [],
    [2,3],
    [1,4,5],
    [1,4,7],
    [2,3,6],
    [2],
    [3,8],
    [3],
    [6],
]

print(bfs(n, adjacency_list, 1))
