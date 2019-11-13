class Solution(object):
    def normalSearch(self, nums, target):
        lb, ub = 0, len(nums) -1
        while lb <= ub:
            mid = (lb + ub) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                ub = mid - 1
            else:
                lb = mid + 1

        return -1

    def search(self, nums, target):
        if nums == []: return -1
        if nums[0] <= nums[-1]:
            return self.normalSearch(nums, target)

        # 比较target与左比较, 锚点
        anchor = nums[0]
        isInLeft = target >= anchor

        lb, ub = 0, len(nums) - 1
        while lb <= ub:
            mid = (lb + ub) // 2
            if nums[mid] == target:
                return mid

            if isInLeft:
                if nums[mid] > target:
                    ub = mid - 1
                else:
                    if nums[mid] < anchor:
                        ub = mid - 1
                    else:
                        lb = mid + 1
            else:
                if nums[mid] < target:
                    lb = mid + 1
                else:
                    if nums[mid] >= anchor:
                        lb = mid + 1
                    else:
                        ub = mid - 1

        return -1


nums = [3, 4, 5, 1, 2]
target = 4

solution = Solution()
x =solution.search(nums, target)
print(x)
