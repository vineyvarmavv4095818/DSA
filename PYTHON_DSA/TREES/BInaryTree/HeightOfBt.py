## Height Of Bonary Tree

class Solution:
    def height(self, root):
        if root is None:
            return 0
        
        left = self.height(root.left)
        right = self.height(root.right)

        return max(left, right) + 1
