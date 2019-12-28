class Solution(object):

    def backtrack(self, s, wordDict, cache = {}):
        if cache.get(s):
            return cache[s]
        result = []
        for length, word in wordDict:
            if s[:length] == word:
                if s[length:] == '':
                    result.append(word)
                else:
                    L1 = self.backtrack(s[length:], wordDict, cache)
                    for one in L1:
                        result.append(word + ' ' + one)

        cache[s] = result
        return result

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """

        length = len(s)
        if length <= 0: return []

        wordDict2 = []
        for word in wordDict:
            wordDict2.append((len(word), word))

        result = self.backtrack(s, wordDict2)

        return result



# s = "catsanddog"
# wordDict = ["cat","cats","and","sand","dog"]

# s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
# wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]

s  = "a"
wordDict = ["b"]

sol = Solution()
x = sol.wordBreak(s, wordDict)
print(x)
