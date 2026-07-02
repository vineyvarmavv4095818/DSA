import heapq

h = []
heapq.heapify(h)

heapq.heappush(h, 1)
heapq.heappush(h, 3)
heapq.heappush(h, 5)
heapq.heappush(h, 7)
heapq.heappush(h, 2)

print(heapq.heappop(h))
# print(heapq.heappop(h))

print(heapq.nlargest(1, h))
print(heapq.nsmallest(1, h))