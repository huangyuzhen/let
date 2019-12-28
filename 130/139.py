class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        length = len(s)
        if length <= 0: return False

        if s in wordDict: return True

        for i in range(1, length):
            if s[:i] in wordDict:
                if self.wordBreak(s[i:], wordDict):
                    return True

        return False

'''
应该会超时，因为有很多重复子问题
应该用动态规划处理
'''


s = "leetcode"
wordDict = ["leet","code"]

s = "applepenapple"
wordDict = ["apple", "pen"]

s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]

# s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
# wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
sol = Solution()
x = sol.wordBreak(s, wordDict)
print(x)
