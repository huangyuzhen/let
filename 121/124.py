# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def ltr(self, node):
        if not node: return 0

        left  = self.ltr(node.left)
        right = self.ltr(node.right)

        # print("node.val:", left, right, node.val)
        self.result = max(left + right + node.val, self.result)
        return max(0, max(left + node.val, right + node.val))

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = -999999
        self.ltr(root)
        return self.result


def initData():
    root = TreeNode(10)
    root.left = TreeNode(9)
    root.right = TreeNode(20)

    # root.left.left = TreeNode(5)
    # root.left.right = TreeNode(1)

    root.right.left = TreeNode(15)
    root.right.right = TreeNode(17)

    # root.left.left.left = TreeNode(7)
    # root.left.left.right = TreeNode(2)

    root.right.right.left  = TreeNode(3)
    root.right.right.right = TreeNode(2)

    return root

root = initData()
solution = Solution()
x = solution.maxPathSum(root)
print(x)
