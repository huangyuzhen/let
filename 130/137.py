class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        b = 0
        ans = 0
        for i in range(32):
            count = 0
            for n in nums:
                if n < 0:
                    b += 1
                    n = -n
                if (n >> i) & 1 == 1:
                    count += 1
            if count % 3 == 1:
                ans = ans| 1 << i
        if b % 3: ans = -ans
        return ans

nums = [2,2,3,2]
nums = [-2,-2,1,1,-3,1,-3,-3,-4,-2]
sol = Solution()
x = sol.singleNumber(nums)
print(x)