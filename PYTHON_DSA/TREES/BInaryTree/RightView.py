from collections import deque


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
    def rightView(self, root):

        if root is None:
            return []
        
        q = deque([root])
        ans = []

        while q:

            size = len(q)

            for i in range(size):

                node = q.popleft()

                # level kki last node
                if i == size - 1:
                    ans.append(node.data)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

        return ans


q = Solution()

print(q.rightView(root))