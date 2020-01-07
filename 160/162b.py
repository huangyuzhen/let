class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        lb, ub = 0, len(nums) -1

        while lb < ub:
            mid = (lb + ub) // 2
            if nums[mid] < nums[mid+1]:
                lb = mid + 1
            else:
                ub = mid

        return lb



nums = [1,2,3,1]
nums = [1,2,1,3,5,6,4]
sol = Solution()
x = sol.findPeakElement(nums)
print(x)