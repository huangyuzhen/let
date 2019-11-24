class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """

        dic = [0, 1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
        string = '123456789'
        result = ''

        k -= 1
        for i in range(n, 0, -1):
            j = k // dic[i]
            result += string[j]
            string = string[:j]+ string[j+1:]
            k = k % dic[i]

        return result


solution = Solution()
x = solution.getPermutation(9, 331987)
print(x)
