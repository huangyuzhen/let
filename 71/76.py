
class Solution(object):
    def isValid(self, found, needs):
        for x in needs:
            if needs[x] > found.get(x, 0):
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
        bestV = [999999999, '']

        needs = {}
        for a in t:
            needs[a] = needs.get(a,0) + 1

        found = {}
        while right < len(s):
            cur = s[right]
            found[cur] = found.get(cur, 0) + 1
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