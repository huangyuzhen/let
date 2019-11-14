'''
二分查找，左闭右开
'''

class Solution(object):
    def leftBoundary(self, nums, target):
        lb, ub = 0, len(nums)
        while lb < ub:
            mid = (lb + ub) // 2
            current = nums[mid]
            if current == target:
                ub = mid
            elif current < target:
                lb = mid + 1
            elif current > target:
                ub = mid

        if lb >= len(nums): return -1
        if nums[lb] == target:
            return lb
        else:
            return -1


    def rightBoundary(self, nums, target):
        lb, ub = 0, len(nums)
        while lb < ub:
            mid = (lb + ub) // 2
            current = nums[mid]
            if current == target:
                lb = mid + 1
            elif current < target:
                lb = mid + 1
            elif current > target:
                ub = mid

        ans = lb - 1
        if ans < 0: return -1
        if nums[ans] == target:
            return ans
        else:
            return -1

    def searchRange(self, nums, target):
        if nums == []: return [-1, -1]

        left = self.leftBoundary(nums, target)
        right = self.rightBoundary(nums, target)

        return [left, right]


nums = []
target = 0

solution = Solution()
x =solution.searchRange(nums, target)
print(x)
