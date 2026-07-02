## Coumt Total Nodes:

class Solution:
    def countNode(self, root):
        if root is None:
            return 0
        
        LeftCount = self.countNode(root.left)
        RightCount = self.countNode(root.right)

        return LeftCount + RightCount +1