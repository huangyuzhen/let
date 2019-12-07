# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root: return

        ls1 = []
        ls2 = []

        stack  = []
        node = root
        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                ls1.append(node)
                ls2.append(node.val)
                node = node.right

        ls2.sort()
        for i in range(len(ls1)):
            ls1[i].val = ls2[i]


def initData():
    root = TreeNode(1)
    root.left = TreeNode(3)
    # root.right = TreeNode(4)

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