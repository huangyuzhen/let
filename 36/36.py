class Solution(object):
    def isValidLine(self, line):
        s = set()
        for one in line:
            if one != ".":
                if one in s:
                    return False
                s.add(one)

        return True

    def isValidSudoku(self, board):
        for i in range(9):
            L = board[i]
            if not self.isValidLine(L):
                return False
            L = []
            for j in range(9):
                L.append(board[j][i])
            if not self.isValidLine(L):
                return False

        Gong = [
            (0,0), (0,3), (0,6),
            (3,0), (3,3), (3,6),
            (6,0), (6,3), (6,6),
        ]
        for idx in Gong:
            L = []
            for i in range(3):
                for j in range(3):
                    L.append(board[i+idx[0]][j+idx[1]])
            if not self.isValidLine(L):
                return False

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
