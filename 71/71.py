class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []

        w = ''
        for s in path + '/':
            if s == '/':
                if w == '..':
                    if len(stack) > 0: stack.pop()
                elif w in '.':
                    pass
                elif w != '':
                    stack.append(w)
                w = ''
            else:
                w += s

        return '/' + '/'.join(stack)



path = "/a//b////c/d//././/.."
solution = Solution()
x = solution.simplifyPath(path)
print(x)