## Check if Two Trees are Identical:

class Solution:

    def idential(self, p, q):
        if p is None and q is None:
            return True
        
        if p is None or q is None:
            return False
        
        if p.data != q.data:
            return False
        
        return self.idential(p.left, q.left) and self.idential(p.right, q.right)