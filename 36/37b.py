class Solution(object):
    def isValid(self, board, m, n):
        row = set()
        for i in range(9):
            num = board[m][i]
            if num in row:
                return False
            elif num != '.':
                row.add(num)

        column = set()
        for i in range(9):
            num = board[i][n]
            if num in column:
                return False
            elif num != '.':
                column.add(num)

        box = set()
        k = (m//3) * 3 + n // 3
        i = (k //3) * 3
        j = (k % 3) * 3
        for ii in range(3):
            for jj in range(3):
                num = board[i+ii][j+jj]
                if num in box:
                    return False
                elif num != '.':
                    box.add(num)

        return True


    def backtrack(self, board, t):
        if t == 81:
            return True

        i, j = t//9, t%9
        if board[i][j] == '.':
            for k in '123456789':
                board[i][j] = k
                if self.isValid(board, i, j) and self.backtrack(board, t+1):
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

board = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]


solution = Solution()
x = solution.solveSudoku(board)
print(x, board)
