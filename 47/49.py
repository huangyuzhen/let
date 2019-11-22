class Solution(object):
    def getKey(self, s):
        k = [0] * 26
        for ch in s:
            idx = ord(ch) - ord('a')
            k[idx] += 1

        return tuple(k)

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        rDict = {}

        for s in strs:
            key = [0] * 26
            for w in s:
                idx = ord(w) - ord('a')
                key[idx] += 1

            key = tuple(key)
            if rDict.get(key):
                rDict[key].append(s)
            else:
                rDict[key] = [s]

        return rDict.values()

    def groupAnagrams1(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 43, 47, 53, 59,
                 61, 67, 71, 73, 79, 83, 89, 97, 101, 103]
        result_dic = {}
        for word in strs:
            keyval = 1
            for w in word:
                keyval *= prime[ord(w)-ord('a')]
            if keyval in result_dic:
                result_dic[keyval].append(word)
            else:
                result_dic[keyval] = [word]
        return result_dic.values()


strings = ["eat", "tea", "tan", "ate", "nat", "bat"]
solution = Solution()
x = solution.groupAnagrams(strings)
print(x)
