class Solution(object):
    def longestValidParentheses(self, s):
        length = len(s)
        # 动态规划,自底向上dp[0]多一位 dp[1] -> s[0]
        dp = [0] * (length+1)

        maxL = 0
        for i in range(1, length):
            if s[i] == ')':
                if s[i-1] == '(':
                    dp[i+1] = dp[i-1] + 2
                elif s[i-1] == ')':
                    n = dp[i]
                    if i-n-1 >= 0 and s[i-n-1] == '(':
                        dp[i+1] = dp[i] + dp[i-n-1] + 2
            if dp[i+1] > maxL:
                maxL = dp[i+1]

        return maxL


s = "(()"

solution = Solution()
x =solution.longestValidParentheses(s)
print(x)
