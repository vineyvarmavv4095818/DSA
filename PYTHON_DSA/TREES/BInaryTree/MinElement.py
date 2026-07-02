## Minimum Element in tree:

class Solution:

    def minimum(self, root):

        if root is None:
            return float('inf')
        
        left = self.minimum(root.left)
        right = self.minimum(root.right)

        return min(root.data, left, right)