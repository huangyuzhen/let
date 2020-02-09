class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k = k % length

        for _ in range(k):
            tmp = nums[-1]
            for i in range(len(nums)-1, 0, -1):
                nums[i] = nums[i-1]
            nums[0] = tmp



nums = [1,2,3,4,5,6,7]
k = 3
sol = Solution()
sol.rotate(nums, k)
print(nums)

