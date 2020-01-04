class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s + ' '
        length = len(s)
        stack = []
        left = 0
        for right in range(length):
            if s[right] == ' ':
                t = s[left:right]
                if t != '':
                    stack.append(t)
                left = right+1

        return ' '.join(stack[::-1])




s = "the sky is blue"
s = "  hello world!  "
s = "a good   example"
sol = Solution()
x = sol.reverseWords(s)
print(x)
