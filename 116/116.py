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
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root: return None

        curLevel = -1
        curTail  = None

        queue = [(0, root)]
        while queue:
            level, node = queue[0]
            queue = queue[1:]
            if level != curLevel:
                curLevel = level
            else:
                curTail.next = node
            curTail = node

            if node.left: queue.append((level+1, node.left))
            if node.right: queue.append((level+1, node.right))

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
