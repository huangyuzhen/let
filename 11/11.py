from typing import List

class Solution:
    def moveRight(self, height, i, j):
        # 从i向右移动指针，找到比i更高的木板位置
        k = i+1
        while k < j and height[k] < height[i]:
           k += 1
        return k

    def moveLeft(self, height, i, j):
        # 从j向左移动指针，找到比j更高的木板位置
        k = j-1
        while k > i and height[k] < height[j]:
            k -= 1
        return k

    def maxArea(self, height: List[int]) -> int:
        length = len(height)
        maxV = 0
        i, j = 0, length-1

        while i<j:
            h = min(height[i], height[j])
            v = h * (j-i)
            # print((i,j) ,v)
            if v > maxV:
                maxV = v

            if height[i] < height[j]:
                i = self.moveRight(height, i, j)
            elif height[i] > height[j]:
                j = self.moveLeft(height, i, j)
            else:
                # 高相等时,移动更快
                i = self.moveRight(height, i, j)
                j = self.moveLeft(height, i, j)

        return maxV


nums = [1,8,6,2,5,4,8,3,7]

s = Solution()
print(s.maxArea(nums))