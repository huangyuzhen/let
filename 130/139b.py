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

        dp = [[0 for _ in range(m+1)] for _ in range(m)]
        for i in range(m): dp[i][i] = 1

        for length in range(1, m+1):
            for i in range(m):
                j = i + length
                if j <= m:
                    if s[i:j] in wordDict:
                        dp[i][j] = 1
                    else:
                        flag = 0
                        for k in range(i, j):
                            if dp[i][k] and dp[k][j]:
                                flag = 1
                                break
                        dp[i][j] = flag

        return dp[0][m] == 1

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
