class Solution(object):
    def sort(self, nums):
        maxVal = max(nums)
        bucket = [0] * (maxVal+1)

        for i in nums:
            bucket[i] = 1

        sort_nums = []
        for j in range(maxVal + 1):
            if bucket[j] != 0:
                sort_nums.append(j)

        return sort_nums


    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length < 2: return 0

        nums = self.sort(nums)
        gap = 0
        for i in range(len(nums) - 1):
            d = nums[i+1] - nums[i]
            gap = max(gap, d)

        return gap


nums = [3,6,9,1]
# nums = [1,10000000]
sol = Solution()
x = sol.maximumGap(nums)
print(x)
