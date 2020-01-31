class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """

        zeroCount = 0
        prod = 1

        for i in range(n):
            prod = prod * (i+1)
            while prod % 10 == 0:
                prod = prod // 10
                zeroCount += 1

        return zeroCount


n = 5
sol = Solution()
x = sol.trailingZeroes(n)
print(x)