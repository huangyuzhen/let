from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        length = len(height)
        maxV = 0
        i = 0
        j = length-1

        while i<j:
            h = min(height[i], height[j])
            v = h * (j-i)
            print((i,j) ,v)
            if v > maxV:
                maxV = v

            if height[i] < height[j]:
                i += 1
            elif height[i] > height[j]:
                j -= 1
            else:
                # 高相等时,移动更快
                i += 1
                j -= 1

        return maxV


nums = [1,8,6,2,5,4,8,3,7]

s = Solution()
print(s.maxArea(nums))