class Solution(object):
    def checkConnect(self, board, m, n, a, b):
        inFlag = True
        visited = set()

        stack = [(a,b)]
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        while stack:
            i,j = stack.pop(0)
            if i == 0 or i == m-1 or j == 0 or j == n-1:
                inFlag = False
            visited.add((i,j))

            for d in directions:
                P = (i + d[0], j + d[1])
                if 0 <= P[0] < m and 0 <= P[1] < n:
                    if board[P[0]][P[1]] == 'O' and P not in visited:
                        stack.append(P)

        if inFlag:
            for P in visited:
                board[P[0]][P[1]] = 'X'

    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        m = len(board)
        if m <= 1: return
        n = len(board[0])

        for i in range(1, m-1):
            for j in range(1, n-1):
                if board[i][j] == 'O':
                    self.checkConnect(board, m, n, i, j)



board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
board = [["O","X","X","X","X","O","O","X","O","X","X","X","X","X","X","O","O","X","X","O"],["O","O","O","O","O","O","X","O","X","O","X","O","O","X","X","O","O","O","X","O"],["O","X","O","X","O","X","O","X","O","O","X","X","X","O","O","O","O","O","O","X"],["X","O","O","X","X","X","X","X","O","X","O","O","O","O","X","O","X","O","X","O"],["O","X","O","O","O","O","X","O","O","O","O","X","O","O","X","O","X","X","X","O"],["O","O","O","O","O","O","O","X","O","X","X","O","O","X","X","O","O","X","O","X"],["O","O","X","X","X","X","O","X","X","X","X","O","O","O","X","O","X","O","X","X"],["X","X","X","X","O","O","X","O","X","O","O","O","O","O","O","X","X","X","O","X"],["X","O","O","O","X","X","O","O","X","O","X","X","O","O","O","X","O","O","O","O"],["X","O","O","X","O","X","O","X","O","O","X","X","X","O","O","O","O","O","X","O"],["O","O","O","X","O","O","X","O","O","O","O","O","O","X","O","X","O","O","X","X"],["O","X","O","O","X","X","X","O","X","X","X","O","O","O","X","O","X","O","O","O"],["X","X","X","O","X","X","O","X","O","X","O","X","X","O","O","O","X","O","O","O"],["O","X","X","O","X","O","O","X","X","O","X","X","O","X","X","O","X","X","O","O"],["O","X","X","O","O","X","O","O","O","X","O","X","O","O","O","O","O","O","X","X"],["O","O","X","O","O","O","X","X","O","X","X","X","X","O","X","O","X","O","X","O"],["X","O","O","O","X","O","X","O","X","O","O","O","O","X","X","O","O","O","O","O"],["X","O","O","X","X","O","O","X","X","O","O","O","X","O","O","O","X","X","X","O"],["O","X","O","X","X","O","O","O","X","X","O","O","X","X","X","O","O","X","X","O"],["O","O","X","O","X","O","O","O","O","O","O","O","O","X","O","X","O","O","X","O"]]

sol = Solution()
sol.solve(board)
print(board)

