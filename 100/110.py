# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def getDepth(self, node):
        if not node: return 0

        left = self.getDepth(node.left)
        right = self.getDepth(node.right)

        if left < 0 or right < 0: return -1
        if left == right + 1 or left + 1 == right or left == right:
            return max(left, right) + 1
        else:
            return -1

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        depth = self.getDepth(root)
        return depth >= 0


def initData():
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)

    # root.left.left = TreeNode(1)
    # root.left.right = TreeNode(3)

    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    return root


root = initData()
solution = Solution()
print(solution.isBalanced(root))
