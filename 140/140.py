class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """

        length = len(s)
        if length <= 0: return []

        result = []
        if s in wordDict:
            result.append(s)

        for i in range(1, length):
            if s[:i] in wordDict:
                for one in self.wordBreak(s[i:], wordDict):
                    result.append(s[:i] + ' ' + one)

        return result



s = "catsanddog"
wordDict = ["cat","cats","and","sand","dog"]

# s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
# wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]

sol = Solution()
x = sol.wordBreak(s, wordDict)
print(x)
