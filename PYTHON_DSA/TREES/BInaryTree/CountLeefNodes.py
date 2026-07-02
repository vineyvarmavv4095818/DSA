## Count Leef Nodes:

class Solution:
    def count(self, root):
        if root is None:
            return 0
        
        if root.left is None and root.right is None:
            return 1
        
        leftCount = self.count(root.left)
        rightCount = self.count(root.right)

        return leftCount + rightCount