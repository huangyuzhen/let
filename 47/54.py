class Solution(object):
    def spiralOrder(self, matrix):
        if matrix == []: return []

        result = []
        M, N=len(matrix), len(matrix[0])
        directions=[(0, 1),(1, 0),(0, -1), (-1, 0)]

        x, y = (0, 0)           # 从 0,0出发
        low, upper  = 0, M      # x in [low, upper) 区间
        left, right = 0, N      # y in [left, right) 区间
        d_index     = 0         # 指示方向

        result.append(matrix[x][y])
        for _ in range(M*N-1):
            d_x, d_y = directions[d_index]
            if low <= x + d_x < upper and left <= y + d_y < right:
                pass
            else:
                if d_index == 0:
                    low +=1
                elif d_index == 1:
                    right -= 1
                elif d_index == 2:
                    upper -= 1
                elif d_index == 3:
                    left += 1

                d_index  = (d_index + 1) % 4
                d_x, d_y = directions[d_index]

            x += d_x
            y += d_y
            result.append(matrix[x][y])

        return result

matrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]

# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
#     ]
# matrix = [[6,9,7]]


solution = Solution()
x = solution.spiralOrder(matrix)
print(x)
