class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        length = len(nums)
        if length == 0: return 0
        if length == 1: return nums[0]

        rotateIndex = 0
        if nums[0] > nums[-1]:
            lb, ub = 0, length - 1
            while lb < ub:
                mid = (lb + ub) // 2
                if nums[mid] > nums[ub]:
                    lb = mid+1
                else:
                    ub = mid
            rotateIndex = lb

        return nums[rotateIndex]



nums = [5,6,7,8,9,10,11,1,2,3,4]
sol = Solution()
x = sol.findMin(nums)
print(x)
