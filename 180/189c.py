class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k = k % length

        if k == 0: return

        # 全部反转
        for i in range(length // 2):
            j = length -i -1
            nums[i], nums[j] = nums[j], nums[i]

        # 翻转前k个
        for i in range(k // 2):
            j = k -i -1
            nums[i], nums[j] = nums[j], nums[i]

        #翻转后n-k个
        for i in range((length-k) // 2):
            start = k+ i
            end = length -i-1
            nums[start], nums[end] = nums[end], nums[start]




nums = [1,2,3,4,5,6]
k = 3
sol = Solution()
sol.rotate(nums, k)
print(nums)

