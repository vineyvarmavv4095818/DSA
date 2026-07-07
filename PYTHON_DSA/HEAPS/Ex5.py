import heapq

def heapSort(arr):

    heap = []

    for i in arr:
        heapq.heappush(heap, i)

    ans = []

    while heap:
        ans.append(heapq.heappop(heap))

    return ans

print(heapSort([2,3,5,4,3,4,5,6,7]))