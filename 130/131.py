class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        length = len(s)
        if length == 0: return [[]]
        elif length == 1: return [[s]]

        result = []
        for i in range(length):
            first = s[:i+1]
            if first == first[::-1]:
                second = s[i+1:]
                if not second:
                    result.append([first])
                else:
                    parts = self.partition(second)
                    for item in parts:
                        item.insert(0, first)
                        result.append(item)

        return result

s = "aaa"
sol = Solution()
x = sol.partition(s)
print(x)
