class Solution(object):
    def sort(self, nums):
        length = len(nums)
        maxVal = max(nums)
        exp = 1

        while maxVal > 0:
            L = [ [] for _ in range(10)]
            for i in range(length):
                index = nums[i] // exp
                index %= 10
                L[index].append(nums[i])

            i = 0
            for index in range(10):
                for n in L[index]:
                    nums[i] = n
                    i += 1

            maxVal = maxVal // 10
            exp *= 10

        return nums


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
nums = [1,10000000]
sol = Solution()
x = sol.maximumGap(nums)
print(x)
