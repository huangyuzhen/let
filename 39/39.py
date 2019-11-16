class Solution(object):
    def saveResult(self, result, t):
        r = []
        for i in range(t+1):
            num = result[i]
            if num != 0:
                r.append(num)
        r.sort()
        self.resultSet.add(tuple(r))

    def backtrack(self, candiates, target, result, t):
        if t == self.maxN: return

        curSum = 0
        for i in range(t):
            curSum += result[i]
        if curSum == target:
            self.saveResult(result, t)
            return

        for number in candiates:
            if number + curSum <= target:
                result[t] = number
                self.backtrack(candiates, target, result, t+1)
            else:
                # 因为排序过，后续再取值一定也会大于target,剪枝
                break

        result[t] = 0
        return

    def combinationSum(self, candidates, target):
        if len(candidates) <= 0: return []
        self.resultSet = set()

        candidates.sort()
        minimal = candidates[0]
        self.maxN = target // minimal + 1

        result = [0] * self.maxN
        self.backtrack(candidates, target, result, 0)

        return self.resultSet










candidates = [2,3,5]
target = 8

solution = Solution()
x =solution.combinationSum(candidates, target)
print(x)
