class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        self.kCount = 0
        def backtrack(string, t, r = []):
            if t == n:
                self.kCount += 1
                # print(self.kCount, r)
                if self.kCount == k:
                    self.result = ''.join(r)
                    return True
                return

            for a in string:
                if a not in r:
                    r[t] = a
                    found = backtrack(string, t+1, r)
                    r[t] = ''
                    if found: return True

            return


        string = '123456789'
        string = string[:n]
        r = [''] * n
        backtrack(string, 0, r)
        return self.result


solution = Solution()
x = solution.getPermutation(3, 4)
print(x)