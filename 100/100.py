class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p == None and q == None: return True
        if p == None or q == None: return False
        if p.val != q.val: return False

        if not self.isSameTree(p.left, q.left): return False
        if not self.isSameTree(p.right, q.right): return False

        return True

    def bfs(self, node):
        m = []
        queue = [node]
        while queue:
            first = queue[0]
            queue = queue[1:]

            if first == None:
                m.append(first)
            else:
                m.append(first.val)
                queue.append(first.right)
                queue.append(first.left)

        return tuple(m)

    def isSameTree2(self, p, q):
        def bfs(node):
            m = []
            queue = [node]
            while queue:
                first = queue[0]
                queue = queue[1:]

                if first == None:
                    m.append(first)
                else:
                    m.append(first.val)
                    queue.append(first.right)
                    queue.append(first.left)

            return tuple(m)
        p_m = bfs(p)
        q_m = bfs(q)
        return p_m == q_m


