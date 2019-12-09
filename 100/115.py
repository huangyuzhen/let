'''
递归
'''
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """

        if t == '' or t == s: return 1
        if len(s) <= len(t): return 0

        num = 0
        n = len(s) - len(t) + 1
        for i in range(n):
            if s[i] == t[0]:
                num += self.numDistinct(s[i+1:], t[1:])
        return num





s = "babgbag"
t = "bag"

# s = "rabbbit"
# t = "rabbit"
sol = Solution()
x = sol.numDistinct(s,t)
print(x)
