class Solution:
    def romanToInt(self, s: str) -> int:
        nDict = {
            "I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000,
            "IV":4, "IX":9, "XL":40, "XC":90, "CD":400, "CM":900
        }

        i = 0
        length = len(s)
        number = 0
        while i < length:
            ns = s[i:i+2]
            if ns in nDict:
                number += nDict[ns]
                i += 2
            else:
                number += nDict[s[i]]
                i += 1

        return number


nums = 'III'


s = Solution()
print(s.romanToInt(nums))