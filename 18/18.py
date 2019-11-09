from typing import List

def transform(nums):
    d = {}
    for i in range(len(nums)):
        k = nums[i]
        d[k] = i

    return d

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        numDict = transform(nums)
        length  = len(nums)
        result  = set()

        for i in range(length):
            if nums[i] >= 0 and nums[i] > target:
                break
            for j in range(i+1, length-2):
                twoSum = nums[i] + nums[j]
                if twoSum >= 0 and ( twoSum > target or nums[j] > target):
                    break

                for k in range(j+1, length-1):
                    threeSum = twoSum + nums[k]
                    if threeSum >= 0 and ( threeSum > target or nums[k] > target):
                        break

                    number = target - threeSum
                    x = numDict.get(number)
                    if x and x > k:
                        result.add((nums[i], nums[j], nums[k], nums[x]))



        return list(result)










nums = [1, 0, -1, 0, -2, 2]
target = 0

# nums = [1,-2,-5,-4,-3,3,3,5]
# target = -11

s = Solution()
print(s.fourSum(nums, target))
