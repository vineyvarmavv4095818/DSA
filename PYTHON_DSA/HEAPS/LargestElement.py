import heapq

def largest(arr):

    heap = []

    for x in arr:
        heapq.heappush(heap, -x)

    return -heapq.heappop(heap)

arr = [5,1,3,10,9]

print(largest(arr))