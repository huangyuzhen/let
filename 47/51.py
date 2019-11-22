class Solution(object):
    def isValid(self, xList, t, j):
        for i in range(len(xList)):
            if i == t or xList[i] == j:
                # 同行或者同列
                return False
            if abs(i - t) == abs(xList[i] - j):
                return False

        return True

    def addResult(self, r):
        q = '.' * self.maxN
        matrix = []
        for i in range(self.maxN):
            j = r[i]
            matrix.append(q[:j] + 'Q' + q[j+1:])

        self.result.append(matrix)

    def backtrack(self, r, t):
        if t == self.maxN:
            self.addResult(r)
            return

        for j in range(self.maxN):
            if self.isValid(r, t, j):
                r.append(j)
                self.backtrack(r, t+1)
                # 回溯
                r.pop()


    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.maxN   = n

        self.result = []
        self.backtrack([], 0)

        return self.result



solution = Solution()
x = solution.solveNQueens(4)
print(len(x))
print(x)
