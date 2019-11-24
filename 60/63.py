class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [
            [0] * n,
            [0] * n,
        ]

        if obstacleGrid[0][0] == 1:
            return 0

        dp[0][0] = 1
        # first row
        for j in range(1, n):
            if obstacleGrid[0][j] == 1:
                dp[0][j] = 0
            else:
                dp[0][j] = dp[0][j-1]

        for i in range(1, m):
            dp[i%2][0] = 1
            if obstacleGrid[i][0] == 1:
                dp[i%2][0] = 0
            else:
                dp[i%2][0] = dp[(i-1)%2][0]

            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i%2][j] = 0
                else:
                    dp[i%2][j] = dp[i%2][j-1] + dp[(i+1)%2][j]

        return dp[(m-1)%2][n-1]


m = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]

m = [[0,0],[1,1],[0,0]]

solution = Solution()
x = solution.uniquePathsWithObstacles(m)
print(x)