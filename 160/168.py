class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """

        strings = "ZABCDEFGHIJKLMNOPQRSTUVWXY"

        s = ''
        while n > 0:
            m = n % 26
            n = n // 26
            if m == 0:
                n -= 1
            s = strings[m] + s

        return s





n = 701
sol = Solution()
x = sol.convertToTitle(n)
print(x)
