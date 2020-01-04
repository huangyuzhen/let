class Solution(object):
    def gcd(self, a, b):
        while b != 0:
            tmp = a % b
            a, b = b, tmp
        return a

    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        length = len(points)
        if length <= 2: return length

        bestV = 0
        for i in range(length):
            A = points[i]
            maxV = 0
            duplicate = 0
            dic = {}

            for j in range(i+1, length):
                B = points[j]
                if B == A:
                    duplicate += 1
                    continue

                x = B[0] - A[0]
                y = B[1] - A[1]

                gcd = self.gcd(x,y)
                # print(A, B, x, y, "get gcd:", gcd)
                key = (x//gcd, y//gcd)
                dic[key] = dic.get(key, 0) + 1
                maxV = max(maxV, dic[key])

            bestV = max(bestV, maxV + duplicate + 1)

        return bestV



# points = [[1,1],[2,2],[3,3]]
# points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
points = [[84,250],[0,0],[1,0],[0,-70],[0,-70],[1,-1],[21,10],[42,90],[-42,-230]]
# points = [[0,0],[0,0]]
# points = [[1,1],[1,1],[1,1]]
sol = Solution()
x = sol.maxPoints(points)
print(x)

