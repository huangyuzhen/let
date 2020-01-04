class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)

        dpMax, dpMin  = 1, 1
        bestV = -9999999

        for i in range(length):
            number = nums[i]
            if number >= 0:
                newMax = max(dpMax * number, number)
                newMin = min(dpMin * number, number)
            else:
                newMax = max(dpMin * number, number)
                newMin = min(dpMax * number, number)

            dpMax, dpMin = newMax, newMin
            bestV = max(bestV, dpMax)

        return bestV

nums = [2,3,-2,4]
# nums = [-2,0,-1]
sol = Solution()
x = sol.maxProduct(nums)
print(x)

'''
动态规划，O(N)
'''