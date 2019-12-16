class Solution(object):
    def findLadders(self, beginWord: str, endWord: str, wordList: list) -> list:
        wordList = set(wordList)
        if endWord not in wordList: return []

        result = []
        visited = set()
        forward  = {beginWord: [[beginWord]]}
        backward = {endWord: [[endWord]]}
        pathL   = 2

        while forward:
            if len(forward) > len(backward):
                forward, backward = backward, forward

            tmp = {}
            while forward:
                word, paths = forward.popitem()
                visited.add(word)

                for i in range(len(word)):
                    for s in 'abcdefghijklmnopqrstuvwxyz':
                        newWord = word[:i] + s + word[i+1:]
                        if newWord in backward: # 连通
                            if paths[0][0] == beginWord:
                                result.extend(fPath + bPath[::-1] for fPath in paths for bPath in backward[newWord])
                            else:
                                result.extend(fPath + bPath[::-1] for fPath in backward[newWord] for bPath in paths)
                        elif newWord in wordList and newWord not in visited:
                            tmp[newWord] = tmp.get(newWord, [])
                            tmp[newWord].extend([path + [newWord] for path in paths])

            pathL += 1
            if result and pathL > len(result[0]):
                break
            forward = tmp
        return result



beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

# beginWord = "qa"
# endWord = "sq"
# wordList = ["si","go","se","cm","so","ph","mt","db","mb","sb","kr",
# "ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra",
# "fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn",
# "au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb",
# "ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di",
# "hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er",
# "sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]


sol = Solution()
x = sol.findLadders(beginWord, endWord,wordList)
print(x)

