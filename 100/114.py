# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root: return

        right = root.right
        if right:
            self.flatten(right)

        left  = root.left
        if left:
            root.left = None

            self.flatten(left)
            tail = left
            while tail.right:
                tail = tail.right
            root.right = left
            tail.right = right




def initData():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(5)

    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)

    # root.right.left = TreeNode(13)
    root.right.right = TreeNode(6)

    # root.left.left.left = TreeNode(7)
    # root.left.left.right = TreeNode(2)

    # root.right.right.left  = TreeNode(5)
    # root.right.right.right = TreeNode(1)

    return root


root = initData()
solution = Solution()
print(solution.flatten(root))

