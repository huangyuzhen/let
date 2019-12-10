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
    def bfs(self, root, node, level):
        if not node.left: return

        tail = root
        h = level
        while h >= 0:
            tail = tail.left
            h -= 1
        while tail.next:
            tail = tail.next

        node.left.next = node.right
        if tail != node.left:
            tail.next = node.left

        self.bfs(root, node.left, level+1)
        self.bfs(root, node.right, level+1)

    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root: return None
        self.bfs(root, root, 0)

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