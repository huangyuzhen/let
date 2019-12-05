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
            self.walk(root.right, result)
            result.append(root.val)

    def postorderTraversal(self, root):
        result = []
        self.walk(root, result)
        return result

    def postorderTraversal1(self, root):
        result = []
        stack  = []
        node = root
        pre  = None
        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack[-1]
                if node.right and node.right != pre:
                    node = node.right
                else:
                    stack.pop()
                    result.append(node.val)
                    pre = node
                    node = None
        return result

    def postorderTraversal2(self, root):
        result = []
        stack = [root]

        while stack:
            node = stack.pop()
            if hasattr(node, 'traversalFlag') and node.traversalFlag:
                del(node.traversalFlag)
                result.append(node.val)
            else:
                node.traversalFlag = True
                stack.append(node)

                if node.right:
                    stack.append(node.right)

                if node.left:
                    stack.append(node.left)

        return result

    def postorderTraversal3(self, root):
        result = []
        stack = [root]

        while stack:
            node = stack.pop()
            if node:
                result.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        return result[::-1]


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
print(solution.postorderTraversal(root))
print(solution.postorderTraversal1(root))
print(solution.postorderTraversal2(root))
print(solution.postorderTraversal3(root))
