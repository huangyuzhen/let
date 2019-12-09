# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0

        depth = 99999
        stack = [(1, root)]

        while stack:
            level, node = stack.pop()
            if not node.left and not node.right:
                if level < depth:
                    depth = level
            else:
                if node.right: stack.append((level+1, node.right))
                if node.left: stack.append((level+1, node.left))

        return depth



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
print(solution.minDepth(root))
