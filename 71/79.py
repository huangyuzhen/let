class Solution(object):
    def walk(self, board, word, m, n, maxN, i, j, visited = [], t = 0):
        if t == maxN-1:
            return True

        visited.append((i,j))
        # 分别向4个方向尝试
        if i-1 >= 0 and (i-1, j) not in visited and board[i-1][j] == word[t+1]:
            if self.walk(board, word, m, n, maxN, i-1, j, visited, t+1):
                return True

        if i+1 < m  and (i+1, j) not in visited and board[i+1][j] == word[t+1]:
            if self.walk(board, word, m, n, maxN, i+1, j, visited, t+1):
                return True

        if j-1 >= 0 and (i, j-1) not in visited and board[i][j-1] == word[t+1]:
            if self.walk(board, word, m, n, maxN, i, j-1, visited, t+1):
                return True

        if j+1 < n  and (i, j+1) not in visited and board[i][j+1] == word[t+1]:
            if self.walk(board, word, m, n, maxN, i, j+1, visited, t+1):
                return True
        # 回溯
        visited.pop()

        return False


    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m = len(board)
        n = len(board[0])
        maxN = len(word)

        self.found = False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if self.walk(board, word, m, n, maxN, i, j):
                        return True

        return False




# board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# word = "SEE"

board = [["a","a"]]
word = "aa"

solution = Solution()
x = solution.exist(board, word)
print(x)