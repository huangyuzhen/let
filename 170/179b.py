class LargerNumKey(str):
    def __lt__(self, y):
        return self + y > y + self

class Solution:
    def largestNumber(self, nums):
        nums = list(map(str, nums))
        nums.sort(key=LargerNumKey)
        result = ''.join(nums)
        if result[0] == '0':
            return '0'
        return result

    def largestNumber2(self, nums):
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num



# nums = [10,2]
nums = [3,30,34,5,9]
nums = [824,938,1399,5607,6973,5703,9609,4398,8247]

sol = Solution()
x = sol.largestNumber(nums)
print(x)