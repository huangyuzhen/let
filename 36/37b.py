class Solution(object):
    # 检查在(m,n)位置是否可以填value
    def isValid(self, board, m, n, value):
        for i in range(9):
            if board[m][i] == value or board[i][n] == value:
                return False

        i = (m // 3) * 3
        j = (n // 3) * 3
        for ii in range(3):
            for jj in range(3):
                if board[i+ii][j+jj] == value :
                    return False
        return True

    def backtrack(self, board, t):
        if t == 81:
            return True

        i, j = t//9, t%9
        if board[i][j] == '.':
            for v in '123456789':
                if self.isValid(board, i, j, v):
                    board[i][j] = v
                    if self.backtrack(board, t+1):
                        return True
            board[i][j] = '.'
        else:
            if self.backtrack(board, t+1):
                return True

        return False

    def solveSudoku(self, board):
        return self.backtrack(board, 0)


board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]


import time
start = time.perf_counter()

solution = Solution()
x = solution.solveSudoku(board)

print(x)
for line in board: print(line)

stop = time.perf_counter()
print("Elapsed time: ", (stop - start))