# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def ltr(self, node):
        if node:
            self.ltr(node.left)
            if self.checkFlag:
                if self.wrong1 is None and self.pre and node.val < self.pre.val:
                    self.wrong1 = self.pre
                    self.wrong2 = node

                if self.wrong1 and node.val > self.wrong1.val:
                    self.wrong2 = self.pre
                    self.checkFlag = False
                    return

            self.pre = node
            self.ltr(node.right)

    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root: return

        self.checkFlag = True
        self.wrong1 = None
        self.wrong2 = None
        self.pre   = None

        self.ltr(root)

        if self.wrong1:
            if self.wrong1.val > self.pre.val:
                self.wrong2 = self.pre
            self.wrong1.val, self.wrong2.val = self.wrong2.val, self.wrong1.val


# [68,41,null,-85,null,-73,-49,-98,null,null,null,-124]

def initData():
    root = TreeNode(1)
    root.left = TreeNode(3)
    # root.right = TreeNode(7)

    # root.left.left = TreeNode(2)
    root.left.right = TreeNode(2)

    # root.right.left = TreeNode(2)
    return root

def LTR(root):
        return LTR(root.left) + [root.val] + LTR(root.right) if root else []

root = initData()
solution = Solution()
print(LTR(root))

solution.recoverTree(root)

print(LTR(root))