class Solution:
    def trailingZeroes(self, n):
        p = 0
        while n > 0:
            n = n // 5
            p += n
        return p


n = 125
sol = Solution()
x = sol.trailingZeroes(n)
print(x)