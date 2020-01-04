class Solution:
    def maxProduct(self, A):
        B = A[::-1]
        for i in range(1, len(A)):
            A[i] *= A[i - 1] or 1
            B[i] *= B[i - 1] or 1
        return max(max(A),max(B))


nums = [2,3,-2,4]
# nums = [-2,0,-1]
# nums = [-3,  4]

sol = Solution()
x = sol.maxProduct(nums)
print(x)
