# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
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

    def bfsWalk(self, root):
        if not root: return []

        result = []
        queue  = [root]
        while queue:
            node = queue[0]
            queue = queue[1:]

            if node == None:
                result.append(None)
                pass
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

    def genTree(self, array, n):
        root = None
        for i in range(n):
            root = self.insertBST(root, array[i])

        bfsWalk = self.bfsWalk(root)
        t = tuple(bfsWalk)
        if t not in self.uniq:
            self.result.append(root)
            self.uniq.add(t)


    def backtrack(self, n, t, current):
        if t == n:
            self.genTree(current, n)
            return

        for i in range(1, n+1):
            if i not in current:
                current.append(i)
                self.backtrack(n, t+1, current)
                current.pop()


    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0: return []

        self.uniq   = set()
        self.result = []
        self.backtrack(n, 0, [])

        # print(self.uniq)
        return self.result



solution = Solution()
print(solution.generateTrees(4))
