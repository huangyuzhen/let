class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        m = len(triangle)
        if m <= 0 : return 0

        dp  = [0] * m
        dp[0] = triangle[0][0]

        dp2 = [0] * m
        for i in range(1, m):
            dp2[0] = dp[0] + triangle[i][0]
            for j in range(1, i+1):
                if j < i:
                    a = min(dp[j-1], dp[j])
                else:
                    a = dp[j-1]
                dp2[j] = a + triangle[i][j]

            dp, dp2 = dp2, dp
        return min(dp)




# tri = [[2],[3,4],[6,5,7],[4,1,8,3]]
tri = [[2],[4,2],[1,4,2]]


# for l in tri: print(l)
# exit

sol = Solution()
x = sol.minimumTotal(tri)
print(x)