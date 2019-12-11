class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        dp = [1]
        for i in range(rowIndex+1):
            result = [1] * (rowIndex+1)
            for j in range(1, i):
                if j+j <= i:
                    result[j] = dp[j] + dp[j-1]
                else:
                    result[j] = result[i-j]
            dp = result

        return dp




sol = Solution()
x = sol.getRow(11)
print(x)