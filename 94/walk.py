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

    def inorderTraversal0(self, root):
        f = self.inorderTraversal0
        return f(root.left) + [root.val] + f(root.right) if root else []

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
            if hasattr(node, 'traversalFlag') and node.traversalFlag:
                del(node.traversalFlag)
                result.append(node.val)
            else:
                if node.right:
                    stack.append(node.right)

                node.traversalFlag = True
                stack.append(node)

                if node.left:
                    stack.append(node.left)

        return result

    def inorderTraversal22(self, root):
        WHITE, GRAY = 0, 1
        result = []
        stack = [(WHITE, root)]
        while stack:
            color, node = stack.pop()
            if not node: continue
            if color == WHITE:
                stack.append((WHITE, node.right))
                stack.append((GRAY, node))
                stack.append((WHITE, node.left))
            else:
                result.append(node.val)

        return result

    def inorderTraversal3(self, root):
        result = []
        node = root

        while node:
            if not node.left:
                result.append(node.val)
                node = node.right
            else:
                newTop = node.left
                node.left = None
                rightMost = newTop
                while rightMost.right:
                    rightMost = rightMost.right
                rightMost.right = node
                node = newTop

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
print(solution.inorderTraversal0(root))
print(solution.inorderTraversal1(root))
print(solution.inorderTraversal2(root))
print(solution.inorderTraversal22(root))
print(solution.inorderTraversal3(root))
