class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        m = len(matrix)
        n = len(matrix[0])

        firstFlag = False

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    if j == 0:
                        firstFlag = True
                    else:
                        matrix[0][j] = 0

        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(n):
                    matrix[i][j] = 0

        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(m):
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for j in range(1, n):
                matrix[0][j] = 0
        if firstFlag:
            for i in range(m):
                matrix[i][0] = 0


        return matrix

m = [
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]

solution = Solution()
x = solution.setZeroes(m)
print(x)