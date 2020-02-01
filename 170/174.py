class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """

        m = len(dungeon)
        n = len(dungeon[0])

        dp = [[0] * n for _ in range(m)]
        dp[-1][-1] = max(1, 1-dungeon[-1][-1])
        for j in range(n-2, -1, -1):
            dp[-1][j] = max(1, dp[-1][j+1]- dungeon[-1][j])

        for i in range(m-2, -1, -1):
            dp[i][-1] = max(1, dp[i+1][-1]- dungeon[i][-1])

        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                # 比较 dp[i][j+1], dp[i+1][j]，选择小的
                select = min(dp[i][j+1], dp[i+1][j])
                dp[i][j] = max(1, select - dungeon[i][j])

        # for line in dp: print(line)
        return dp[0][0]



# dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
dungeon = [[1,-3,3],[0,-2,0],[-3,-3,-3]]
sol = Solution()
x = sol.calculateMinimumHP(dungeon)
print(x)
