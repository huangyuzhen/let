# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def dfs(self, node, r = 0):
        if not node: return r

        r += node.val
        if not node.left and not node.right:
            self.count += r
            return

        if node.left:
            self.dfs(node.left, r*10)
        if node.right:
            self.dfs(node.right, r*10)

    def sumNumbers(self, root):
        self.count = 0
        self.dfs(root, 0)

        return self.count




def initData():
    root = TreeNode(4)
    root.left = TreeNode(9)
    root.right = TreeNode(0)

    # root.left.left = TreeNode(5)
    # root.left.right = TreeNode(1)

    # root.right.left = TreeNode(13)
    # root.right.right = TreeNode(6)

    # root.left.left.left = TreeNode(7)
    # root.left.left.right = TreeNode(2)

    # root.right.right.left  = TreeNode(5)
    # root.right.right.right = TreeNode(1)

    return root

root = initData()
solution = Solution()
print(solution.sumNumbers(root))

