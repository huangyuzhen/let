# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generate(self, ls):
        if not ls: return [None]
        result = []
        for i in range(len(ls)):
            leftTrees  = self.generate(ls[:i])
            rightTrees = self.generate(ls[i+1:])
            for leftNode in leftTrees:
                for rightNode in rightTrees:
                    root = TreeNode(ls[i])
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
        ls = list(range(1,n+1))
        return self.generate(ls)



def bfsWalk(root):
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

solution = Solution()
res = solution.generateTrees(0)
for root in res:
    print(bfsWalk(root))
