'''
二分查找, 闭区间
'''

class Solution(object):
    def leftBoundary(self, nums, target):
        lb, ub = 0, len(nums)-1
        while lb <= ub:
            mid = (lb + ub) // 2
            current = nums[mid]
            if current == target:
                ub = mid -1
            elif current < target:
                lb = mid + 1
            elif current > target:
                ub = mid -1

        if lb >= len(nums): return -1
        if nums[lb] == target:
            return lb
        else:
            return -1


    def rightBoundary(self, nums, target):
        lb, ub = 0, len(nums) -1
        while lb <= ub:
            mid = (lb + ub) // 2
            current = nums[mid]
            if current == target:
                lb = mid + 1
            elif current < target:
                lb = mid + 1
            elif current > target:
                ub = mid - 1

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


nums = [5,7,7,8,8,10]
target = 8

solution = Solution()
x =solution.searchRange(nums, target)
print(x)
