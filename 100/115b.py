'''
递归，有备忘录
'''

class Solution(object):

    def num(self, s, t, sIndex, tIndex):
        key = (sIndex, tIndex)
        if self.memTable.get(key): return self.memTable[key]

        if t[tIndex:] == '' or t[tIndex:] == s[sIndex:]:
            self.memTable[key] = 1
            return 1

        n = len(s[sIndex:]) - len(t[tIndex])
        if n <= 0:
            self.memTable[key] = 0
            return 0

        num = 0
        for i in range(n+1):
            if s[sIndex+i] == t[tIndex]:
                num += self.num(s, t, sIndex+i+1, tIndex+1)

        self.memTable[key] = num
        return num

    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        self.memTable = {}

        num = self.num(s, t, 0, 0)
        return num





s = "babgbag"
t = "bag"

# s = "rabbbit"
# t = "rabbit"
sol = Solution()
x = sol.numDistinct(s,t)
print(x)
