# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def walk(self, root, result):
        if root:
            result.append(root.val)
            self.walk(root.left, result)
            self.walk(root.right, result)

    def preorderTraversal(self, root):
        result = []
        self.walk(root, result)
        return result

    def preorderTraversal1(self, root):
        result = []
        stack  = []
        node = root
        while node or stack:
            if node:
                result.append(node.val)
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                node = node.right
        return result

    def preorderTraversal2(self, root):
        result = []
        stack = [root]

        while stack:
            node = stack.pop()
            if hasattr(node, 'traversalFlag') and node.traversalFlag:
                del(node.traversalFlag)
                result.append(node.val)
            else:
                if node.right:
                    stack.append(node.right)

                if node.left:
                    stack.append(node.left)

                node.traversalFlag = True
                stack.append(node)

        return result

    def preorderTraversal3(self, root):
        result = []
        stack = [root]

        while stack:
            node = stack.pop()
            if node:
                result.append(node.val)
                stack.append(node.right)
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
print(solution.preorderTraversal(root))
print(solution.preorderTraversal1(root))
print(solution.preorderTraversal2(root))
print(solution.preorderTraversal3(root))
