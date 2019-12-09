# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def walk(self, node, sum):
        sum -= node.val
        if not node.left and not node.right:
            return sum == 0

        flag = False
        if not flag and node.left:
            flag = self.walk(node.left, sum)
        if not flag and node.right:
            flag = self.walk(node.right, sum)

        return flag

    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root: return False
        return self.walk(root, sum)





def initData():
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)

    root.left.left = TreeNode(11)
    # root.left.right = TreeNode(3)

    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)

    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)

    # root.left.right.left  = TreeNode(2)
    root.right.right.right = TreeNode(1)

    return root


root = initData()
solution = Solution()
print(solution.hasPathSum(root, 22))
