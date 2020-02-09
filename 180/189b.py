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

        count = 0
        start = 0
        while count < length:
            preIndex, preValue = start, nums[start]
            while True:
                index = (preIndex + k) % length
                value = nums[index]
                nums[index] = preValue

                preIndex, preValue = index, value
                count += 1
                if start == preIndex: break

            start += 1



nums = [1,2,3,4,5,6]
k = 4
sol = Solution()
sol.rotate(nums, k)
print(nums)

