def bulidGraph(n, edges):

    graph = [[] for _ in range(n)]

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    return graph

n = 5

edges = [
    (0,1),
    (0,2),
    (1,3),
    (2,4)
]

print(bulidGraph(n, edges))


