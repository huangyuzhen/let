class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        length = len(nums)
        if length == 0: return 0
        if length == 1: return nums[0]

        lb, ub = 0, length -1
        while lb < ub:
            mid = (lb + ub) // 2
            if nums[mid] >  nums[ub]:
                lb = mid+1
            elif nums[mid] < nums[ub]:
                ub = mid
            else:
                ub -= 1

        return nums[lb]




nums = [2,2,3,3,0,1,2]
# nums = [1,1,1,3,1]

sol = Solution()
x = sol.findMin(nums)
print(x)
