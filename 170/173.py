# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        L = []
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()
            L.append(cur.val)
            cur = cur.right

        self.L = L
        self.length = len(L)
        self.index = 0

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        if self.hasNext():
            val = self.L[self.index]
            self.index += 1
            return val
        else:
            return None


    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return self.index < self.length


def initData():
    a0 = TreeNode(7)
    a0.left = TreeNode(3)
    a0.right = TreeNode(15)

    a2 = a0.right
    a2.left = TreeNode(9)
    a2.right = TreeNode(20)

    return a0

root = initData()

# Your BSTIterator object will be instantiated and called as such:
obj = BSTIterator(root)
obj.next()
obj.hasNext()
