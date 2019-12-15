class Solution(object):
    def isNeightbor(self, word1, word2):
        length = len(word1)
        diffCount = 0
        i = 0
        while i < length and diffCount <= 1:
            if word1[i] != word2[i]:
                diffCount += 1
            i += 1
        return diffCount <= 1

    def backtrace(self, beginWord, endWord, wordList, wordLadders):
        if beginWord == endWord:
            length = len(wordLadders)
            print(wordLadders)
            if self.bestL == 0 or length < self.bestL:
                self.bestL  = length
                self.result = [tuple(wordLadders)]
            elif self.bestL == length:
                self.result.append(tuple(wordLadders))
            return

        for s in wordList:
            if s not in wordLadders and self.isNeightbor(beginWord, s):
                wordLadders.append(s)
                self.backtrace(s, endWord, wordList, wordLadders)
                wordLadders.pop()


    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        if endWord not in wordList: return []

        self.bestL  = 0
        self.result = []
        self.backtrace(beginWord, endWord, wordList, [beginWord])

        return self.result




# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log","cog"]

beginWord = "qa"
endWord = "sq"
wordList = ["si","go","se","cm","so","ph","mt","db","mb","sb","kr",
"ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra",
"fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn",
"au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb",
"ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di",
"hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er",
"sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]

sol = Solution()
x = sol.findLadders(beginWord, endWord,wordList)
print(x)
