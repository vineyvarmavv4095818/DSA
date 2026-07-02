# kth largest element in array

import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        h = []

        for x in nums:
            heapq.heappush(h, x)
            if len(h) > k:
                heapq.heappop(h)

        return h[0]

nums = [3, 2, 1, 9, 6, 4]
k = 2

obj = Solution()
ans = obj.findKthLargest(nums, k)

print("Kth Largest Element =", ans)