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

solution = Solution()
x =solution.isValidSudoku(board)
print(x)
