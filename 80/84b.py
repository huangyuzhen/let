class Solution(object):
    def largestRectangleArea(self, heights):
        if not heights: return 0

        stack   = [0]
        heights = [-1] + heights + [0]

        length = len(heights)
        bestV  = 0

        for i in range(1, length):
            cur = heights[i]
            if cur >= heights[stack[-1]]:
                stack.append(i)
                # print("a", stack)
            else:
                while cur <= heights[stack[-1]]:
                    j = stack.pop()
                    h = heights[j]
                    w = i - stack[-1] - 1
                    area = h * w
                    bestV = max(bestV, area)
                    # print("bestV", j, h, w, area)
                stack.append(i)
                # print("b", stack)

        return bestV



heights = [2,1,5,6,2,3]
solution = Solution()
x = solution.largestRectangleArea(heights)
print(x)