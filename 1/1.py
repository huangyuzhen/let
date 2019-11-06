'''
'''
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        d = {}
        for i in range(length):
            d[nums[i]] = i

        for i in range(length):
            n = target - nums[i]
            if d.get(n) and d[n] != i:
                return [i, d[n]]

        return None


nums = [2, 7, 11, 15]
target = 9

s = Solution()
print(s.twoSum(nums, target))
