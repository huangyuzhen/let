class Solution(object):
    def isValidSudoku(self, board):
        rows = [{} for i in range(9)]
        columns = [{} for i in range(9)]
        boxes = [{} for i in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    #  i j
                    k = (i // 3) * 3 + j // 3

                    if rows[i].get(num):
                        return False
                    if columns[j].get(num):
                        return False
                    if boxes[k].get(num):
                        return False

                    rows[i][num] = 1
                    columns[j][num] = 1
                    boxes[k][num] = 1

        return True


    def backtrack(self, board, t):
        if t == 81:
            return True

        i, j = t//9, t%9
        if board[i][j] == '.':
            for k in '123456789':
                board[i][j] = k
                if self.isValidSudoku(board) and self.backtrack(board, t+1):
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
