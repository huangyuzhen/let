from collections import Counter

class Solution(object):
    def isValid(self, found, needs):
        for x in needs:
            if needs[x] > found[x]:
                return False
        return True

    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t: return ''

        left, right = 0, 0
        bestV = [9999, '']


        needs = Counter(t)
        found = Counter()

        while right < len(s):
            cur = s[right]
            found[cur] += 1
            right += 1

            while self.isValid(found, needs):
                if right - left < bestV[0]:
                    bestV = [right-left, s[left:right]]

                cur = s[left]
                found[cur] -= 1
                left += 1

        return bestV[1]



solution = Solution()
S = "ADOBECODEBANC"
T = "ABC"
x = solution.minWindow(S, T)
print(x)