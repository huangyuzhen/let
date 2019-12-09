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
        dp_first  = [1] * (m+1)
        dp_second = [0] * (m+1)

        for i in range(1, n+1):
            for j in range(i, m+1):
                # t[i-1], s[j-1], dp[i][j]
                if t[i-1] == s[j-1]:
                    dp_second[j] = dp_first[j-1] + dp_second[j-1]
                else:
                    dp_second[j] = dp_second[j-1]
            if i < n:
                dp_first  = dp_second
                dp_second = [0] * (m+1)

        return dp_second[m]



s = "babgbag"
t = "bag"

s = "rabbbit"
t = "rabbit"
sol = Solution()
x = sol.numDistinct(s,t)
print(x)
