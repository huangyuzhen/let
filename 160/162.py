class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        length = len(nums)
        index = 0


        while index < length-1:
            if nums[index] > nums[index+1]:
                return index
            else:
                index += 1

        return index



nums = [1,2,3,1]
nums = [1,2,1,3,5,6,4]
sol = Solution()
x = sol.findPeakElement(nums)
print(x)