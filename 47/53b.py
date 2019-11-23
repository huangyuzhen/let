'''
动态规划
dp[i], 以第i个元素为结尾的子数组的最大和
'''

class Solution:
    def maxSubArray(self, nums):
        size = len(nums)
        if size == 0:
            return 0
        dp = [0] * size
        dp[0] = nums[0]

        for i in range(1, size):
            if dp[i - 1] > 0:
                dp[i] = dp[i - 1] + nums[i]
            else:
                dp[i] = nums[i]

        return max(dp)

nums = [-2,1,-3,4,-1,2,1,-5,4]
solution = Solution()
x = solution.maxSubArray(nums)
print(x)
