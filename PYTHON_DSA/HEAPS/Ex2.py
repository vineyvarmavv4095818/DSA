# kth smallest element in array:

import heapq

class Solution(object):
    def findKthSmallest(self, nums, k):
        h = []

        for x in nums:
            heapq.heappush(h, -x)
            
            if len(h) > k:
                heapq.heappop(h)

        return -h[0]

nums = [3, 2, 1, 9, 6, 4]
k = 2

obj = Solution()
ans = obj.findKthSmallest(nums, k)

print("Kth Smallest Element =", ans)