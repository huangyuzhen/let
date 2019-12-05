# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def walk(self, root, result):
        if root:
            self.walk(root.left, result)
            result.append(root.val)
            self.walk(root.right, result)

    def inorderTraversal(self, root):
        result = []
        self.walk(root, result)
        return result

    def bfsWalk(self, root):
        if not root: return []

        result = []
        queue  = [root]
        while queue:
            node = queue[0]
            queue = queue[1:]

            if node == None:
                result.append(None)
            else:
                result.append(node.val)
                if node.left:
                    queue.append(node.left)
                else:
                    queue.append(None)
                if node.right:
                    queue.append(node.right)
                else:
                    queue.append(None)

        while result[-1] == None:
            result.pop()

        return result

    def insertBST(self, root, n):
        if not root:
            return TreeNode(n)

        if root.val == n:
            return False
        elif root.val < n:
            right = self.insertBST(root.right, n)
            if not right: return False
            root.right = right
        elif root.val > n:
            left = self.insertBST(root.left, n)
            if not left: return False
            root.left = left
        return root


def initData():
    root = TreeNode(3)
    root.left = TreeNode(2)
    root.left.left = TreeNode(1)

    return root


root = initData()
solution = Solution()
print(solution.inorderTraversal(root))
print(solution.bfsWalk(root))

# x = solution.insertBST(root, 4)
# if x:
#     print('ok')
#     print(solution.inorderTraversal(x))
# else:
#     print('bad')
