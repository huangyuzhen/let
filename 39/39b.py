'''
'''
class Solution(object):
    def backtrack(self, candiates, target, result = []):
        if target == 0:
            self.resultList.append(tuple(result))

        for number in candiates:
            if result[-1:] and number < result[-1]:
                continue

            if number <= target:
                result.append(number)
                self.backtrack(candiates, target - number, result)
                result.pop()
        return

    def combinationSum(self, candidates, target):
        if len(candidates) <= 0: return []
        self.resultList = []

        candidates.sort()
        self.backtrack(candidates, target)

        return self.resultList


candidates = [2,3,5]
target = 8

solution = Solution()
x =solution.combinationSum(candidates, target)
print(x)
