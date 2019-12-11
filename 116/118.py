class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0: return []

        dp = [[1]]
        for i in range(2, numRows+1):
            r = [1] * i
            last  = dp[i-2]
            for j in range(1,i-1):
                if j +j < i:
                    r[j] = last[j-1] + last[j]
                else:
                    r[j] = r[i-j-1]
            dp.append(r)
        return dp





sol = Solution()
x = sol.generate(12)

for line in x: print(line)
