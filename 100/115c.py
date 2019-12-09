'''
动态规划
'''
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m, n = len(s), len(t)
        dp = [[1] * (m+1)]
        for _ in range(n): dp.append([0] * (m+1))

        for i in range(1, n+1):
            for j in range(i, m+1):
                # t[i-1], s[j-1], dp[i][j]
                total = 0
                if t[i-1] == s[j-1]:
                    total += dp[i-1][j-1]
                total += dp[i][j-1]

                dp[i][j] = total

        # for line in dp:print(line)
        return dp[n][m]



s = "babgbag"
t = "bag"

s = "rabbbit"
t = "rabbit"
sol = Solution()
x = sol.numDistinct(s,t)
print(x)
