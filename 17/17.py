from typing import List

class Solution:
    def gen(self, digits, prefix = []):
        if len(digits) <= 0:
            return prefix

        first = digits[0]
        result = []
        if len(prefix) <= 0:
            for s in self.keyMaps[first]:
                result.append(s)
        else:
            for s in self.keyMaps[first]:
                for a in prefix:
                    result.append(a+s)

        return self.gen(digits[1:], result)

    def letterCombinations(self, digits: str) -> List[str]:
        self.keyMaps = {
            "1":"!@#",
            "2":"abc", "3":"def", "4":"ghi", "5":"jkl",
            "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"
        }

        return self.gen(digits)




digits = "23"

s = Solution()
print(s.letterCombinations(digits))
