## Search An Element:

class Solution:
    def search(self, root, tar):
        if root is None:
            return False
        
        if root.data == tar:
            return True
        
        leftCheck = self.search(root.left, tar)
        rightCheck = self.search(root.rigth, tar)

        return leftCheck or rightCheck