class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        count = len(nums) // 2

        d = {}
        for n in nums:
            d[n] = d.get(n,0) + 1
            if d[n] > count:
                return n

        return None



nums = [2,2,1,1,1,2,2]
nums = [3,2,3]
sol = Solution()
x = sol.majorityElement(nums)
print(x)
