## Maximum Element in tree:

class Solution:

    def maximum(self, root):

        if root is None:
            return float('-inf')
        
        left = self.maximum(root.left)
        right = self.maximum(root.right)

        return max(root.data, left, right)