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
        if endWord not in wordList: return 0

        L = len(beginWord)
        # wordList 预处理
        linkDict = self.buildLinkDict([beginWord] + wordList, L)

        visited = set()
        forward = {beginWord}
        backward = {endWord}
        pathL = 2

        while forward:
            if len(forward) > len(backward): # bfs总是展开短的一端
                forward, backward = backward, forward

            tmp = set()
            while forward:
                word = forward.pop()
                visited.add(word)
                for i in range(L):
                    w = word[:i] + '*' + word[i+1:]
                    for newWord in linkDict[w]:
                        if newWord == word or newWord in visited:
                            continue
                        if newWord in backward:
                            return pathL
                        tmp.add(newWord)
            pathL += 1
            forward = tmp

        return 0



beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]


sol = Solution()
x = sol.ladderLength(beginWord, endWord, wordList)
print(x)
