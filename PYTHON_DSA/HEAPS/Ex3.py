## Sort a Nearly Sorted Array:

import heapq

def sortK(arr, k):

    heap = []
    ans = []

    for x in arr:

        heapq.heappush(heap, x)

        if len(heap) > k:
            ans.append(heapq.heappop(heap))

    while heap:
        ans.append(heapq.heappop(heap))

    return ans

arr = [6,4,3,1,2,5]
k=3

print(sortK(arr, k))