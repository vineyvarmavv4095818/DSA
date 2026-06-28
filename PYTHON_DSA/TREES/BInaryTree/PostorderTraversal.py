## Binary Tree Postorder Traversal

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
        
        stack1 = [root]
        stack2 = []
        ans = []

        while stack1:
            node = stack1.pop()
            stack2.append(node)

            if node.left:
                stack1.append(node.left)

            if node.right:
                stack1.append(node.right)


        while stack2:
            ans.append(stack2.pop().data)

        return ans

sol = Solution()
print(sol.preorderTraversal(root))