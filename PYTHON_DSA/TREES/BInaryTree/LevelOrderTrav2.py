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
    def level_order(self, node):
        res = []
        q = deque([])
        q.append(node)

        while q:
            e = q.popleft()
            res.append(e.data)

            if e.left is not None:
                q.append(e.left)

            if e.right is not None:
                q.append(e.right)

        

        return res[::-1]


queue = Solution()

print(queue.level_order(root))