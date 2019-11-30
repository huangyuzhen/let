class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix: return 0

        m = len(matrix)
        n = len(matrix[0])

        row = []
        for _ in range(m): row.append([0] * n)
        for i in range(m):
            row[i][0] = int(matrix[i][0])

        column = []
        for _ in range(m): column.append([0] * n)
        for j in range(n):
            column[0][j] = int(matrix[0][j])

        maxArea = 0
        for i in range(m):
            for j in range(n):
                area = 0
                if matrix[i][j] == '0':
                    row[i][j]    = 0
                    column[i][j] = 0
                else:
                    if j > 0:
                        row[i][j]    = row[i][j-1] + 1
                    if i > 0:
                        column[i][j] = column[i-1][j] + 1

                    if i == 0:
                        area = row[i][j]
                    elif j == 0:
                        area = column[i][j]
                    else:
                        k = j
                        h = column[i][k]

                        while k >= 0:
                            h = min(h, column[i][k])
                            if h == 0: break
                            w = j-k +1
                            area = max(h * w, area)
                            k -= 1

                maxArea = max(area, maxArea)

        return maxArea


m = [
    ["1","0","1","0","0"],
    ["1","0","1","1","1"],
    ["1","1","1","1","1"],
    ["1","0","0","1","0"]]
solution = Solution()
x = solution.maximalRectangle(m)
print(x)