class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """

        if numerator == 0: return '0'

        t = ''
        if numerator < 0:
            if denominator < 0:
                denominator = -denominator
            else:
                t = '-'
            numerator = -numerator
        else:
            if denominator < 0:
                t = '-'
                denominator = -denominator

        t += '{}'.format(numerator // denominator)
        r = numerator % denominator
        if r == 0: return t

        index = 0
        remain = {}
        remain[r] = index

        s = ''
        a = r * 10
        while a:
            index += 1
            s += '{}'.format(a // denominator)
            r = a % denominator

            if r in remain:
                index = remain[r]
                s = s[:index] + '(' + s[index:] + ')'
                break

            remain[r] = index
            a = r * 10
        return t + '.' + s



numerator = -50
denominator = 8
sol = Solution()
x = sol.fractionToDecimal(numerator, denominator)
print(x)
