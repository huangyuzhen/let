class Solution(object):
    def buildLinkDict(self, wordList, L):
        dic = {}
        for word in wordList:
            for i in range(L):
                w = word[:i] + '*' + word[i+1:]
                if dic.get(w):
                    dic[w].append(word)
                else:
                    dic[w] = [word]
        return dic

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        L = len(beginWord)
        linkDict = self.buildLinkDict([beginWord] + wordList, L)

        queue = [(beginWord, 1)]
        visited = set()
        while queue:
            word, N = queue.pop(0)
            if word == endWord: return N
            visited.add(word)
            for i in range(L):
                w1 = word[:i] + '*' + word[i+1:]
                for w2 in linkDict[w1]:
                    if w2 not in visited:
                        queue.append((w2, N+1))
                linkDict[w1] = []

        return 0




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
x = sol.ladderLength(beginWord, endWord, wordList)
print(x)

