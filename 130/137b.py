class Solution:
    def singleNumber(self, nums):
        dic = {
            (0,0): (0,1),
            (0,1): (1,0),
            (1,0): (0,0)
        }

        v = [(0,0)] * 32
        flag   = 0
        result = 0

        for n in nums:
            if n < 0:
                flag += 1
                n = -n
            for i in range(32):
                if n >> i & 1:
                    v[i] = dic[v[i]]

        result = 0
        for i in range(32):
            result += v[i][1] << i

        if flag % 3 == 1:
           return -result

        return result



nums = [2,2,3,2]
nums = [-2,-2,1,1,-3,1,-3,-3,-4,-2]

sol = Solution()
x = sol.singleNumber(nums)
print(x)