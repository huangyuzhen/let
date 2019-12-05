# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
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

    def generate(self, left, right):
        result = []

        if left > right:
            result.append(None)
            return result

        for i in range(left, right+1):
            leftTrees  = self.generate(left, i-1)
            rightTrees = self.generate(i+1, right)

            for leftNode in leftTrees:
                for rightNode in rightTrees:
                    root = TreeNode(i)
                    root.left = leftNode
                    root.right = rightNode

                    result.append(root)

        return result


    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0: return []
        return self.generate(1, n)




solution = Solution()
res = solution.generateTrees(4)
for root in res:
    print(solution.bfsWalk(root))
