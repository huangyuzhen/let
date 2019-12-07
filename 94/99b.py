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

        stack  = []
        pre = None
        wrong = None

        cur = root
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()

                if wrong is None and pre and cur.val < pre.val:
                    wrong = pre
                if wrong and cur.val > wrong.val:
                    break

                pre = cur
                cur = cur.right

        if wrong and wrong.val > pre.val:
            pre.val, wrong.val = wrong.val, pre.val


def initData():
    root = TreeNode(3)
    root.left = TreeNode(4)
    root.right = TreeNode(7)

    # root.left.left = TreeNode(2)
    # root.left.right = TreeNode(2)

    root.right.left = TreeNode(2)
    return root

def LTR(root):
        return LTR(root.left) + [root.val] + LTR(root.right) if root else []

root = initData()
solution = Solution()
print(LTR(root))

solution.recoverTree(root)

print(LTR(root))