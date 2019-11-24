class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        dp = [
            [1] * n,
            [1] * n,
        ]

        for i in range(1, m):
            dp[i%2][0] = 1
            for j in range(1, n):
                dp[i%2][j] = dp[i%2][j-1] + dp[(i+1)%2][j]

        return dp[(m-1)%2][n-1]



solution = Solution()
x = solution.uniquePaths(3, 2)
print(x)