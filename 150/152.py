class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        bestV  = -99999999

        for i in range(length):
            dp1 = 1
            maxV = -99999999
            for j in range(i, length):
                dp2 = dp1 * nums[j]
                maxV = max(maxV, dp2)
                dp1 = dp2

            bestV = max(bestV, maxV)

        return bestV

nums = [2,3,-2,4]
sol = Solution()
x = sol.maxProduct(nums)
print(x)