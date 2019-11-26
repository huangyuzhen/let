class Solution(object):
    def gotoState(self, state, s):
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
        if s == ' ':
            return transfer[state][0]
        elif s == '+' or s == '-':
            return transfer[state][1]
        elif '0' <= s <= '9':
            return transfer[state][2]
        elif s == '.':
            return transfer[state][3]
        elif s == 'e' or s == 'E':
            return transfer[state][4]
        else:
            return -1

    def isNumber(self, string):
        """
        :type s: str
        :rtype: bool
        """
        state = 0
        for s in string:
            state = self.gotoState(state, s)
            if state < 0:
                break

        return state in [1, 4, 6, 8]



s = ".44.8"
solution = Solution()
x = solution.isNumber(s)
print(x)
