class Solution(object):
    def longestValidParentheses(self, s):
        stack = [('', 0)]
        length = len(s)

        record = [0] * length
        for i in range(length):
            cur = s[i]
            if cur == ')' and stack[-1][0] == '(':
                r = stack.pop()
                record[i] = 1
                record[r[1]] = 1
            else:
                stack.append((cur, i))

        maxL = 0
        left, right = -1, 0
        while right < length:
            if record[right] == 0:
                if left >= 0:
                    maxL = max(maxL, right-left)
                left =-1
            else:
                if left < 0:
                    left = right
            right += 1

        if left >= 0:
            maxL = max(maxL, right-left)

        return maxL



s = "(()"

solution = Solution()
x =solution.longestValidParentheses(s)
print(x)
