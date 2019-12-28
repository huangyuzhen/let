class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        m = len(s)
        if m <= 0: return False
        if s in wordDict: return True

        dp = [1] + [0] * m
        for i in range(1, m+1):
            flag = 0
            for k in range(i):
                if dp[k] and s[k:i] in wordDict:
                    flag = 1
                    break
            dp[i] = flag

        # print(dp)
        return dp[m] == 1

'''
应该会超时，因为有很多重复子问题
应该用动态规划处理
'''


# s = "leetcode"
# wordDict = ["leet","code"]

s = "applepenapple"
wordDict = ["apple", "pen"]

# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]

# s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
# wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
sol = Solution()
x = sol.wordBreak(s, wordDict)
print(x)
