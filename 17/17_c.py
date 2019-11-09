from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keyMaps = {
            "1":"!@#",
            "2":"abc", "3":"def", "4":"ghi", "5":"jkl",
            "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"
        }

        if digits == "":
            return []

        L = ['']
        for digit in digits:
            M = []
            for s in keyMaps[digit]:
                for one in L:
                    M.append(one+s)
            L = M

        return L



digits = "23"

s = Solution()
print(s.letterCombinations(digits))
