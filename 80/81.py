class Solution:
    def search(self, nums, target):
        lb, ub = 0, len(nums) - 1
        while lb <= ub:
            mid = (lb + ub) // 2
            if nums[mid] == target or nums[lb] == target or nums[ub] == target:
                return True

            if nums[mid] == nums[lb]:
                if nums[mid] == nums[ub]:
                    lb += 1
                    ub -= 1
                else:
                    lb = mid + 1
            elif nums[mid] < nums[lb]:
                if target < nums[mid] or target > nums[lb]:
                    ub = mid - 1
                else:
                    lb = mid + 1
            elif nums[mid] > nums[lb]:
                if target < nums[lb] or target > nums[mid]:
                    lb = mid + 1
                else:
                    ub = mid - 1

        return False



nums = [3,5,1]
target = 1

solution = Solution()
x =solution.search(nums, target)
print(x)
