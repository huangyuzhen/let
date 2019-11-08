from typing import List

class Solution:
    def sumBackTrack(self, t = 0, count = 0, currentSum = 0, xList = []):
        if count == 3 and currentSum == 0:
            xList.sort()
            self.result.add(tuple(xList))
            return
        if count > 3 or t == self.length:
            return
        # 选择此元素
        number = self.nums[t]
        self.sumBackTrack(t+1, count + 1, currentSum + number, xList + [number])
        # 不选择
        self.sumBackTrack(t+1, count, currentSum, xList[::])

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.length = len(nums)
        self.result = set()

        self.sumBackTrack(0)

        return self.result



nums = [-1, 0, 1, 2, -1, -4]

s = Solution()
print(s.threeSum(nums))
