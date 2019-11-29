class Solution(object):
    def backtrack(self, nums, maxN, result, start = 0, t = 0):
        self.result.append(tuple(result[:t]))
        if t == maxN:
            return

        for i in range(start, maxN):
            result[t] = nums[i]
            self.backtrack(nums, maxN, result, i+1, t+1)

    def subsets(self, nums):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        maxN = len(nums)
        self.result = []
        self.backtrack(nums, maxN, [0] * maxN, )

        return self.result




nums = [1,2,3]
solution = Solution()
x = solution.subsets(nums)
print(x)