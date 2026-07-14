## Dijkstra Algorithm

import heapq

def dijkstra(edges, V, src):
    
    graph = [[] for _ in range(V)]
    for u,v,d in edges:
        graph[u].append([v,d])
    
    distance = [float['inf'] for _ in range(V)]
    distance[src] = 0

    q = [[0,src]]

    while q:
        curr_dist, node = heapq.heappop(q)

        if curr_dist > distance[node]:
            continue

        for neighbour, weight in graph[node]:
            dist_trav = curr_dist + weight

            if dist_trav < distance[neighbour]:
                distance[neighbour] = dist_trav

                heapq.heappush(q, [dist_trav, neighbour])

        return distance
