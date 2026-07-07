## Top K frequent Element

from collections import Counter

import heapq

def topK(nums, k):

    freq = Counter(nums)

    heap = []

    for num, count in freq.items():
        heapq.heappush(heap, (count,num))

        if len(heap)>k:
            heapq.heappop(heap)

    ans = []

    while heap:
        ans.append(heapq.heappop(heap)[1]) # yaha [1] -> actual num ke liye # [0] -> frequency ke liye

    return ans[::-1]

print(topK([1,1,1,1,4,4,4,4,3,2,2,5,5,5,5], 1))