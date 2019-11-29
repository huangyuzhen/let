class Solution(object):
    def backtrack(self, n, k, result, t = 0):
        if t == k:
            self.result.append(tuple(result))
            return

        for i in range(t+1, n+1):
            if t > 0 and i <= result[t-1]:
                continue
            result[t] = i
            self.backtrack(n, k, result, t+1)

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        self.result = []
        self.backtrack(n, k, [0] * k)

        return self.result





solution = Solution()
x = solution.combine(4,2)
print(x)