import heapq

class Solution:

    def dijkstra(self, V, edges, src):

        graph = [[] for _ in range(V)]
        for u,v,d in edges:
            graph[u].append([v,d])

        distance = [float("inf") for _ in range(V)]
        distance[src] = 0

        priority_queue = [[0,src]]

        while priority_queue:
            curr_dist,node = heapq.heappop(priority_queue)

            if curr_dist > distance[node]:
                continue

            for neighbour, weight in graph[node]:
                dist_trav = curr_dist + weight

                if dist_trav < distance[neighbour]:
                    distance[neighbour] = dist_trav

                    heapq.heappush(priority_queue, [dist_trav,neighbour])

        return distance

