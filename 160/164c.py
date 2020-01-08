class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2: return 0

        minVal = min(nums)
        maxVal = max(nums)

        if maxVal - minVal == 0:
            return 0

        gapVal = maxVal - minVal
        interval = gapVal // (n-1)
        if gapVal % (n-1) != 0: interval += 1

        bucketMin = [9999999999] * (n-1)
        bucketMax = [-1] * (n-1)

        for i in range(n):
            if nums[i] == minVal or nums[i] == maxVal:
                continue
            index = (nums[i] - minVal) // interval
            bucketMin[index] = min(bucketMin[index], nums[i])
            bucketMax[index] = max(bucketMax[index], nums[i])

        maxGap = 0
        preMax = minVal
        for index in range(n-1):
            if bucketMax[index] == -1:
                continue
            maxGap = max(bucketMin[index]-preMax, maxGap)
            preMax = bucketMax[index]

        maxGap = max(maxVal-preMax, maxGap)

        return maxGap


nums = [3,6,9,1]
# nums = [1,10000000]
nums = [0, 3, 4, 6, 23, 28, 29, 33, 38, 39]
# nums = [1, 3, 4, 10]
nums = [1,2,3,4,5,6,6,7,6,7,9]


sol = Solution()
x = sol.maximumGap(nums)
print(x)
