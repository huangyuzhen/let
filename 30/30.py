from typing import List

class Solution(object):
    def findSubstring(self, s, words):
        if len(words) <=0 :
            return []

        length = len(words[0])
        count  = len(words)

        allLength = length * count
        dic = {}
        for t in words:
            if dic.get(t):
                dic[t] = dic[t]+1
            else:
                dic[t] = 1

        result = []
        for i in range(len(s) - allLength + 1):
            newDic = {}
            for j in range(count):
                start = i + j * length
                end   = start + length
                sub = s[start:end]

                wordCount = newDic.get(sub, 0)
                if wordCount+1 > dic.get(sub, 0):
                    break

                newDic[sub] = wordCount

            else:
                result.append(i)

        return result



s = "barfoobthefoobarman"

words = ["foo","bar"]

solution = Solution()
print(solution.findSubstring(s, words))
