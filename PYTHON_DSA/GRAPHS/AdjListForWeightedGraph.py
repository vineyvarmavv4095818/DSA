def Adj_list(n, edges):

    adj_list = [[] for _ in range(n)]

    for u,v,d in edges:

        adj_list[u].append([v,d])
        adj_list[v].append([u,d])

    return adj_list

n = 5

edges = [
    (0,1,5),
    (0,2,2),
    (1,3,6),
    (2,4,2)
]

print(Adj_list(n, edges))
