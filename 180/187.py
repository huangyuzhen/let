class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        d = {}
        for i in range(len(s)-9):
            s10 = s[i:i+10]
            d[s10] = d.get(s10, 0) + 1

        L = filter(lambda x: d[x] > 1, d)
        return list(L)



s = "AACCGGAACCGGAACCGG"
sol = Solution()
x = sol.findRepeatedDnaSequences(s)
print(x)