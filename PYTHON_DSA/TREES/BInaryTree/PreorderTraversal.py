## Binary Tree Preorder Traversal

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(5)
root.left.left = Node(4)

class Solution:
    def preorderTraversal(self, root):
        if root is None:
            return
        
        stack = [root]
        ans = []

        while stack:
            node = stack.pop()
            ans.append(node.data)

            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)

        return ans

sol = Solution()
print(sol.preorderTraversal(root))