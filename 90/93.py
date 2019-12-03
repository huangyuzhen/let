class Solution(object):
    def backtrack(self, s, r, t = 0):
        if t == 4:
            if s == '':
                self.result.add('.'.join(r))
            return

        if s == '': return
        if t == 3 and int(s) > 255: return

        if s[0] == '0':
            r.append('0')
            self.backtrack(s[1:], r, t+1)
            r.pop()
            return

        length = min(3, len(s))
        for i in range(length):
            segment = s[:i+1]
            if int(segment) > 255:
                break
            r.append(segment)
            self.backtrack(s[i+1:], r, t+1)
            r.pop()

            if s[0] == '0':
                break


    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.result = set()

        self.backtrack(s, [])

        return list(self.result)




s = "25525511135"
s = "0000"
solution = Solution()
x = solution.restoreIpAddresses(s)
print(x)