class Solution(object):
    def search(self, L, level, beginSet, endSet, meets):
        if len(beginSet) == 0 or len(endSet) == 0:
            return 0

        meets = meets - beginSet
        nextLevelSet = set()
        for word in beginSet:
            for i in range(L):
                for a in 'abcdefghijklmnopqrstuvwxyz':
                    newWord = word[:i] + a + word[i+1:]
                    if newWord not in meets: continue
                    if newWord in endSet: return level+1
                    nextLevelSet.add(newWord)

        if len(nextLevelSet) <= len(endSet):
            beginSet = nextLevelSet
        else:
            beginSet, endSet = endSet, nextLevelSet

        return self.search(L, level+1, beginSet, endSet, meets)


    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList: return 0
        if endWord == beginWord: return 2

        L = len(beginWord)
        return self.search(L, 1, {beginWord}, {endWord}, set(wordList))



beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]


sol = Solution()
x = sol.ladderLength(beginWord, endWord, wordList)
print(x)
