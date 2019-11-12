class Solution(object):
    def reverse(self, nums, start, end):
        i, j = start, end
        while i<j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        length = len(nums)
        if length <= 1:
            return nums

        # 找到左边位置
        idx = length-2
        while idx >= 0 :
            # 比较 nums[n]与nums[n-1]
            if nums[idx] < nums[idx+1]:
                break
            idx -= 1

        # 找右边位置
        if idx >= 0:
            j = idx + 1
            while j < length:
                if nums[j] <= nums[idx]:
                    break
                j += 1
            j -= 1
            nums[j], nums[idx] = nums[idx], nums[j]

        self.reverse(nums, idx+1, length-1)


nums = [1,5,1]

solution = Solution()
solution.nextPermutation(nums)
print(nums)
