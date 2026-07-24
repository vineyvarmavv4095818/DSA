class Solution:
    def permute(self, nums):
        result = []

        def backtrack(path):
            if len(path) == len(nums):
                result.append(path.copy())
                return
            
            for i in nums:
                if i not in path:
                    path.append(i)
                    backtrack(path)
                    path.pop()

        backtrack([])
        return result
    