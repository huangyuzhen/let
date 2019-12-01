class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        G = [0]
        for i in range(n):
            add = 1 << i
            length = len(G)
            for n in range(length-1, -1, -1):
                G.append(G[n] + add)

        return G





solution = Solution()
x = solution.grayCode(4)
print(x)