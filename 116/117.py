'''
拉拉链解法
'''

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
    def nextFirst(self, node):
        r = node
        while r:
            if r.left: return (r, r.left)
            if r.right: return (r, r.right)
            r = r.next

        return None, None

    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root: return None

        # 通过 pre 这层的next， 连接起下一层的next
        pre, first = self.nextFirst(root)
        while first:
            cur = first
            while pre:
                if pre.left and cur != pre.left:
                    cur.next = pre.left
                    cur = cur.next
                if pre.right and cur != pre.right:
                    cur.next = pre.right
                    cur = cur.next
                pre = pre.next

            pre, first = self.nextFirst(first)

        return root


def initData():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)

    root.left.left = Node(4)
    root.left.right = Node(5)

    # root.right.left = Node(6)
    root.right.right = Node(7)

    return root


root = initData()
sol = Solution()
x = sol.connect(root)


while x:
    p = x
    print("#")
    while p:
        print(p.val)
        p = p.next
    x = x.left