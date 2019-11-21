class Solution(object):
    def backtrack(self, nums, t = 0, one = [], visited = []):
        if t == self.maxN:
            self.result.append(tuple(one))
            return

        uniq = set()
        for i in range(self.maxN):
            if i in visited or nums[i] in uniq:
                continue
            uniq.add(nums[i])
            visited.append(i)
            one.append(nums[i])
            self.backtrack(nums, t+1, one, visited)
            one.pop()
            visited.pop()

    def permuteUnique(self, nums):
        N = len(nums)
        if N <= 0:
            return nums

        nums.sort()

        self.maxN   = N
        self.result = []

        t = 0
        self.backtrack(nums, t)

        return self.result



nums = [2]
solution = Solution()
x = solution.permuteUnique(nums)
print(x)
