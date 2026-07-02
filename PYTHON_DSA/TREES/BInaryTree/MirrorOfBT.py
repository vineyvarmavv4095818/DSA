## Mirror of Binary Tree

class Solution:

    def mirror(self, root):
        if root is None:
            return 0
        
        root.left, root.right = root.right, root.left

        ## Ye bhi likh sakte hain:
        
        # temp = root.left
        # root.left = root.right
        # root.right = temp

        self.mirror(root.left)
        self.mirror(root.right)