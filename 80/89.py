class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        if n == 0: return [0]
        if n == 1: return [0, 1]

        G = [[0], [1]]
        for _ in range(2, n+1):
            g = []
            for e in G:
                a = [0]
                for f in e:
                    a.append(f)
                g.append(a)

            r = []
            for e in G[::-1]:
                a = [1]
                for f in e:
                    a.append(f)
                r.append(a)

            G = g + r

        return G





solution = Solution()
x = solution.grayCode(4)
print(x)