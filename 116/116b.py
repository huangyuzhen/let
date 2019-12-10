"""
# Definition for a Node.
"""
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution(object):
    def bfs(self, node, level):
        if self.dict.get(level):
            tail = self.dict[level]
            tail.next = node
        self.dict[level] = node

        if node.left: self.bfs(node.left, level+1)
        if node.right: self.bfs(node.right, level+1)

    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root: return None

        self.dict = {}
        self.bfs(root, 0)

        return root




def initData():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)

    root.left.left = Node(4)
    root.left.right = Node(5)

    root.right.left = Node(6)
    root.right.right = Node(7)

    return root

root = initData()
sol = Solution()
x = sol.connect(root)



while x:
    p = x
    print("start")
    while p:
        print(p.val)
        p = p.next
    x = x.left