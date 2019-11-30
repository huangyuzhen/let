class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length <= 2: return length

        left, right = 0, 0
        while right < length:
            if nums[right] == nums[left]:
                if right - left == 2:
                    nums.pop(right)
                    length -= 1
                else:
                    right += 1
            else:
                left = right
                right += 1

        return length



nums = [0,0,1,1,1,1,2,3,3]
solution = Solution()
x = solution.removeDuplicates(nums)
print(x)
