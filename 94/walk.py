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

    def inorderTraversal1(self, root):
        result = []
        stack  = []
        node = root
        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                result.append(node.val)
                node = node.right
        return result

    def inorderTraversal2(self, root):
        result = []
        stack = [root]

        while stack:
            node = stack.pop()
            if hasattr(node, 'inorderFlag') and node.inorderFlag:
                result.append(node.val)
            else:
                if node.right:
                    stack.append(node.right)

                node.inorderFlag = True
                stack.append(node)

                if node.left:
                    stack.append(node.left)

        return result



def initData():
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(6)

    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)

    root.right.left = TreeNode(5)
    root.right.right = TreeNode(7)
    return root


root = initData()
solution = Solution()
print(solution.inorderTraversal(root))
print(solution.inorderTraversal1(root))
print(solution.inorderTraversal2(root))

