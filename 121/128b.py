class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1: return len(nums)

        maxL = 0
        dic = dict([(x, True) for x in nums])
        for number in nums:
            if not dic[number]: continue
            left = number
            while dic.get(left-1):
                left -= 1
                dic[left] = False
            right = number
            while dic.get(right+1):
                right += 1
                dic[right] = False
            maxL = max(maxL, right-left + 1)

        return maxL


nums = [1,3,2]
sol = Solution()
x = sol.longestConsecutive(nums)
print(x)


'''
贪心算法
'''