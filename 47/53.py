'''
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def maxSubArray(self, nums):
        n = len(nums)

        tmp = nums[0] # 局部最优解
        maxV = tmp    # 整体最优解

        for i in range(1,n):
            if tmp > 0:
                tmp += nums[i]
            else:
                tmp = nums[i]

            if tmp > maxV:
                maxV = tmp

        return maxV


nums = [-2,1,-3,4,-1,2,1,-5,4]
solution = Solution()
x = solution.maxSubArray(nums)
print(x)
