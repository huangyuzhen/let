class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        dp = [[0] * n,[0] * n]
        dp[0][0] = grid[0][0]
        # first row
        for j in range(1,n):
            dp[0][j] = grid[0][j] + dp[0][j-1]

        for i in range(1, m):
            dp[i%2][0] = grid[i][0] + dp[(i-1)%2][0]
            for j in range(1, n):
                dp[i%2][j] = grid[i][j] + min(dp[(i-1)%2][j], dp[i%2][j-1])

        return dp[(m-1)%2][n-1]

    def minPathSum2(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        dp = [[9999999] * n, [9999999] * n]

        for i in range(m):
            if i == 0:
                dp[0][0] = grid[0][0]
            else:
                dp[i%2][0] = grid[i][0] + dp[(i-1)%2][0]

            for j in range(1, n):
                dp[i%2][j] = grid[i][j] + min(dp[(i-1)%2][j], dp[i%2][j-1])

        return dp[(m-1)%2][n-1]

m = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]

s = Solution()
x = s.minPathSum2(m)
print(x)
