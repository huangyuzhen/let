class Solution(object):
    def __init__(self):
        self.memTable = {}

    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        if length <= 1: return 0
        if s == s[::-1]: return 0

        if self.memTable.get(s) != None:
            return self.memTable[s]

        bestV = 99999
        for i in range(1, length):
            first = s[:i]
            if first == first[::-1]:
                minV  = self.minCut(s[i:])
                bestV = min(bestV, minV + 1)

        self.memTable[s] = bestV

        return bestV


s = "aab"
s = "fifgbeajcacehiicccfecbfhhgfiiecdcjjffbghdidbhbdbfbfjccgbbdcjheccfbhafehieabbdfeigbiaggchaeghaijfbjhi"

sol = Solution()
x = sol.minCut(s)
print(x)

# for k in sol.memTable:
#     print(k, sol.memTable[k])