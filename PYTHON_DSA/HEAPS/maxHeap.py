import heapq

max_h = []

heapq.heapify(max_h)

heapq.heappush(max_h, -10)
heapq.heappush(max_h, -8)
heapq.heappush(max_h, -2)
heapq.heappush(max_h, -5)

# print(-heapq.heappop(max_h))
# print(-heapq.heappop(max_h))

print(heapq.nlargest(1,max_h))