class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """

        bestV  = 0
        length = len(heights)

        for i in range(length):
            currH = heights[i]

            left = i
            while left >= 0 and heights[left] >= heights[i]:
                left -= 1

            right = i
            while right < length and heights[right] >= heights[i]:
                right += 1

            currW = right - left - 1
            currArea = currW * currH

            if currArea > bestV:
                bestV = currArea

        return bestV


heights = [2,1,5,6,2,3]
solution = Solution()
x = solution.largestRectangleArea(heights)
print(x)