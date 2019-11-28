class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        m = len(matrix)
        n = len(matrix[0])

        iSet = set()
        jSet = set()

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    iSet.add(i)
                    jSet.add(j)

        for i in range(m):
            for j in range(n):
                if i in iSet or j in jSet:
                    matrix[i][j] = 0

        return matrix

m = [
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]

solution = Solution()
x = solution.setZeroes(m)
print(x)