class Solution(object):
    def getStateIndex(self, s):
        if s == ' ':
            return 0
        elif s == '+' or s == '-':
            return 1
        elif '0' <= s <= '9':
            return 2
        elif s == '.':
            return 3
        elif s == 'e' or s == 'E':
            return 4
        else:
            return -1

    def isNumber(self, string):
        """
        :type s: str
        :rtype: bool
        """
        transfer = [
            [0, 2, 1, 3, -1],
            [8, -1, 1, 4, 5],
            [-1, -1, 1, 3, -1],
            [-1, -1, 4, -1, -1],
            [8,  -1, 4, -1, 5],
            [-1, 7, 6, -1, -1],
            [8, -1, 6, -1, -1],
            [-1, -1, 6, -1, -1],
            [8, -1, -1, -1, -1]
        ]

        state = 0
        for s in string:
            idx = self.getStateIndex(s)
            if idx < 0:
                return False
            state = transfer[state][idx]
            if state < 0:
                return False

        return state in [1, 4, 6, 8]



s = ".. "
solution = Solution()
x = solution.isNumber(s)
print(x)
