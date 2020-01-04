class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)

        dp = [[0] * length for _ in range(length)]
        maxV = -999999
        for i in range(length):
            dp[i][i] = nums[i]
            maxV = max(maxV, dp[i][i])

        for j in range(1, length):
            for i in range(length-j):
                dp[i][i+j] = dp[i][i+j-1] * nums[i+j]
                maxV = max(maxV, dp[i][i+j])
                # print((i,i+j), dp[i][i+j])

        for line in dp: print(line)
        return maxV

nums = [2,3,-2,4]
sol = Solution()
x = sol.maxProduct(nums)
print(x)

'''
解答超时
'''