class Solution(object):
    def backtrack(self, nums, maxN, result, start = 0, t = 0):
        self.result.append(tuple(result[:t]))
        if t == maxN:
            return

        visited = None
        for i in range(start, maxN):
            if nums[i] != visited:
                visited = nums[i]
                result[t] = nums[i]
                self.backtrack(nums, maxN, result, i+1, t+1)

    def subsetsWithDup(self, nums):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        nums.sort()
        maxN = len(nums)
        self.result = []
        self.backtrack(nums, maxN, [0] * maxN)

        return self.result




nums = [4,4,4,1,4]
solution = Solution()
x = solution.subsetsWithDup(nums)
print(x)