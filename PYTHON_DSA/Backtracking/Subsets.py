class Solution:
    def subsetSums(self, nums):
        result = []

        def solve(index, total):
            if index >= len(nums):
                result.append(total)
                return
            
            # pick
            Sum = total + nums[index]
            solve(index + 1, Sum)
            # not pick
            Sum = total
            solve(index + 1, Sum)
            
        solve(0, 0)
        return result
