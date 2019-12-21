class Solution:
    def minCut(self, s: str) -> int:
        length = len(s)
        if length <= 1: return 0

        dp = [[0] * length for _ in range(length)]
        for i in range(length): dp[i][i] = 1
        for j in range(1, length):
            for i in range(j):
                dp[i][j] = 0
                if s[i] == s[j]:
                    if i+2 <= j:
                        dp[i][j] = dp[i+1][j-1]
                    else:
                        dp[i][j] = 1

        resultDp = [0] * length
        for j in range(1, length):
            if dp[0][j]:
                resultDp[j] = 0
            else:
                # 枚举分割点
                minV = 9999999
                for i in range(j):
                    if dp[i+1][j]:
                        minV = min(resultDp[i], minV)
                resultDp[j] = minV + 1

        return resultDp[-1]


s = "aab"
s = "fifgbeajcacehiicccfecbfhhgfiiecdcjjffbghdidbhbdbfbfjccgbbdcjheccfbhafehieabbdfeigbiaggchaeghaijfbjhi"

# s = "fifgbbga"

sol = Solution()
x = sol.minCut(s)
print(x)