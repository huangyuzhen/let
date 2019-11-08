from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        i, j = 0, len(height)-1

        while i<j:
            w = j-i
            h_i, h_j = height[i], height[j]

            if h_i <= h_j:
                area = w * h_i
                k = i+1
                while k < j and height[k] < h_i:
                    k += 1
                i = k
                
            if h_i >= h_j:
                area = w * h_j
                k = j-1
                while k > i and height[k] < h_j:
                    k -= 1
                j = k
            
            maxArea = max(area, maxArea)
            
        return maxArea


nums = [1,8,6,4,5,3,8,3,7]

s = Solution()
print(s.maxArea(nums))