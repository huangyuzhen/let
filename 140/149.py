class Solution(object):
    def __init__(self):
        self.dic = {}

    def isInLine(self, A, B, C):
        L = sorted([A,B,C])
        key = tuple(L)
        if self.dic.get(key) != None:
            return self.dic[key]

        # (y2-y1)/(x2-x1) == (y3-y1)/(x3-x1)
        L1 = (B[1]-A[1]) * (C[0]-A[0])
        L2 = (C[1]-A[1]) * (B[0]-A[0])
        r  = L1 == L2

        # print("check line:", key, r)
        self.dic[key] = r
        return r

    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        length = len(points)
        if length <= 2: return length

        bestV = 0
        for i in range(length-1):
            A = tuple(points[i])
            for j in range(i+1, length):
                B = tuple(points[j])
                if B == A:
                    count = 3
                else:
                    count = 0
                    for k in range(length):
                        C = tuple(points[k])
                        if self.isInLine(A,B,C):
                            count += 1

                bestV = max(bestV, count)

        return bestV



# points = [[1,1],[2,2],[3,3]]
points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# points = [[84,250],[0,0],[1,0],[0,-70],[0,-70],[1,-1],[21,10],[42,90],[-42,-230]]
# points = [[0,0],[0,0]]
# points = [[1,1],[1,1],[1,1]]
sol = Solution()
x = sol.maxPoints(points)
print(x)

