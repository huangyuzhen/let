class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """

        for i in range(len(nums)):
            nums[i] = str(nums[i])

        def helper(a, b):
            x = a + b
            y = b + a
            if x < y:
                return 1
            elif x > y:
                return -1
            else:
                return 0

        nums.sort(cmp=helper)
        s = ''.join(nums)
        if s[0] == '0':
            return '0'
        else:
            return s






# nums = [10,2]
nums = [3,30,34,5,9]
nums = [824,938,1399,5607,6973,5703,9609,4398,8247]

sol = Solution()
x = sol.largestNumber(nums)
print(x)
