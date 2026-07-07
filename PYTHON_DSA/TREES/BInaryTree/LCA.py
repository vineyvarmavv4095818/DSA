## Lowest Common Ancestor (LCA)

class Solution:

    def lca(self, root, p, q):

        # base cases
        if root is None:
            return None
        
        if root.data == p and root.data == q:
            return root
        
        left = self.lca(root.left, p, q)
        right = self.lca(root.right, p, q)

        if left and right:
            return root
        
        return left if left else right