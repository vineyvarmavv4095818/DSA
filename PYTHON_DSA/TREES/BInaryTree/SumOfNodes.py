## Sum of All Nodes:

class Solution:
    def sum(self, root):
        if root is None:
            return 0
        
        left = self.sum(root.left)
        right = self.sum(root.right)

        return left + right + root.data
    