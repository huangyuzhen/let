class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        stack = []
        for token in tokens:
            if token in ('+-*/'):
                n2 = stack.pop()
                n1 = stack.pop()

                if token == '+':
                    number = n1 + n2
                elif token == '-':
                    number = n1 - n2
                elif token == '*':
                    number = n1 * n2
                elif token == '/':
                    number = int(n1 / n2)

                # print(n1, token, n2, '=', number)
                stack.append(number)
            else:
                stack.append(int(token))

        return stack.pop()



tokens = ["2","1","+","3","*"]
tokens = ["4", "13", "5", "/", "+"]
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
sol = Solution()
x = sol.evalRPN(tokens)
print(x)
