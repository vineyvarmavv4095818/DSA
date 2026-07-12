def iterative_dfs(start, graph):
    visited = [False] * len(graph)
    stack = [start]

    while stack:
        node = stack.pop()

        if not visited[node]:
            visited[node] = True
            print(node, end=" ")

            for neighbour in reversed(graph[node]):
                if not visited[neighbour]:
                    stack.append(neighbour)

graph = [
    [1, 2],
    [0, 3],
    [0, 3],
    [1, 2]
]

iterative_dfs(0, graph)