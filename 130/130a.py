class Solution(object):
    def checkConnect(self, board, m, n, a, b):
        stack = [(a,b)]
        # 方向 上右下左
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        board[a][b] = 'C'

        while stack:
            i, j = stack.pop()

            for d in directions:
                a, b = (i + d[0], j + d[1])
                if 0 <= a < m and 0 <= b < n:
                    if board[a][b] == 'O':
                        board[a][b] = 'C'
                        stack.append((a,b))

    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        m = len(board)
        if m <= 1: return
        n = len(board[0])

        # 检查上下
        for i in (0, m-1):
            for j in range(n):
                if board[i][j] == 'O':
                    self.checkConnect(board, m, n, i, j)

        # 检查左右
        for i in range(0, m-1):
            for j in (0, n-1):
                if board[i][j] == 'O':
                    self.checkConnect(board, m, n, i, j)

        # 重新
        table = {'C':'O', 'O':'X', 'X':'X'}
        for i in range(m):
            for j in range(n):
                board[i][j] = table[board[i][j]]


board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
board = [
['X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'] ,
['O', 'X', 'O', 'O', 'O', 'O', 'X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'X'] ,
['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X'] ,
['O', 'O', 'X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'O'] ,
['O', 'O', 'O', 'O', 'O', 'X', 'O', 'O', 'O', 'O', 'X', 'O', 'O', 'O', 'O', 'O', 'X', 'O', 'O', 'X'] ,
['X', 'O', 'O', 'O', 'X', 'O', 'O', 'O', 'O', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O'] ,
['O', 'O', 'O', 'O', 'X', 'O', 'O', 'X', 'O', 'O', 'O', 'O', 'O', 'X', 'O', 'O', 'X', 'O', 'O', 'O'] ,
['X', 'O', 'O', 'O', 'X', 'X', 'X', 'X', 'X', 'O', 'O', 'O', 'O', 'X', 'X', 'O', 'X', 'O', 'O', 'O'] ,
['O', 'O', 'O', 'O', 'O', 'X', 'X', 'X', 'X', 'O', 'O', 'O', 'O', 'X', 'O', 'O', 'X', 'O', 'O', 'O'] ,
['X', 'O', 'O', 'O', 'O', 'X', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'X', 'O', 'O', 'X', 'O', 'O', 'X'] ,
['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'O', 'O', 'X', 'O', 'O', 'O', 'X', 'O', 'X'] ,
['O', 'O', 'O', 'O', 'X', 'O', 'X', 'O', 'O', 'X', 'X', 'O', 'O', 'O', 'O', 'O', 'X', 'O', 'O', 'O'] ,
['X', 'X', 'O', 'O', 'O', 'O', 'O', 'X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'] ,
['O', 'X', 'O', 'X', 'O', 'O', 'O', 'X', 'O', 'X', 'O', 'O', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'O'] ,
['O', 'O', 'X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'O', 'O', 'O', 'O', 'O', 'X', 'X', 'X', 'O'] ,
['X', 'X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'O', 'X', 'X', 'O', 'O', 'O', 'X', 'O', 'O'] ,
['O', 'O', 'X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'O', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'O'] ,
['O', 'O', 'O', 'X', 'O', 'O', 'O', 'O', 'O', 'X', 'X', 'X', 'O', 'O', 'X', 'O', 'O', 'O', 'X', 'O'] ,
['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'] ,
['X', 'O', 'O', 'O', 'O', 'X', 'O', 'O', 'O', 'X', 'X', 'O', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'O'] ,
]


board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

sol = Solution()
sol.solve(board)
for line in board: print(line)

