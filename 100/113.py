# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def backtrace(self, node, sum, r):
        sum -= node.val
        if not node.left and not node.right and sum == 0:
            self.result.append(tuple(r))
            return

        if node.left:
            r.append(node.left.val)
            self.backtrace(node.left, sum, r)
            r.pop()

        if node.right:
            r.append(node.right.val)
            self.backtrace(node.right, sum, r)
            r.pop()

        return

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """

        if not root: return []

        self.result = []
        self.backtrace(root, sum, [root.val])

        return self.result





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

    root.right.right.left  = TreeNode(5)
    root.right.right.right = TreeNode(1)

    return root


root = initData()
solution = Solution()
print(solution.pathSum(root, 22))
