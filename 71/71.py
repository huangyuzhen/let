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
                # check w
                if w == '..':
                    if len(stack) > 0: stack.pop()
                elif w == '.':
                    pass
                elif w != '':
                    stack.append(w)
                w = ''
            else:
                w += s

        if len(stack) == 0:
            return '/'
        else:
            p = ''
            for s in stack:
                p += '/' + s
            return p



path = "/a//b////c/d//././/.."
solution = Solution()
x = solution.simplifyPath(path)
print(x)