class Solution(object):
    def backtrack(self, candiates, target, result = [], t = 0):
        if target == 0:
            self.resultList.append(tuple(result))

        visited = []
        for i in range(t, len(candiates)):
            number = candiates[i]
            if number in visited or (result[-1:] and number < result[-1]):
                continue

            if number <= target:
                visited.append(number)
                result.append(number)
                self.backtrack(candiates, target - number, result, i+1)
                result.pop()
        return

    def combinationSum2(self, candidates, target):
        if len(candidates) <= 0: return []
        self.resultList = []

        candidates.sort()
        self.backtrack(candidates, target)

        return self.resultList


candidates = [10,1,2,7,6,1,5]
target = 8

solution = Solution()
x = solution.combinationSum2(candidates, target)
print(x)