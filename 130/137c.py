class Solution:
    def testF(self, a, b, n):
        newB = b ^ n & ~a
        newA = a ^ n & ~newB
        return newA, newB

    def singleNumber(self, nums):
        a, b = 0, 0
        for n in nums:
            a, b = self.testF(a, b, n)

        return b



def testFunction():
    tests = [
        (0,0),(0,1),(1,0)
        ]
    sol = Solution()

    for n in (0,1):
        for i in range(3):
            a,b = tests[i]
            newA, newB = sol.testF(a,b,n)
            print(a, b, "\t", n, "\t", newA, newB)

testFunction()

# nums = [2,2,3,2,3,1,3]
nums = [-2,-2,1,1,-3,1,-3,-3,-4,-2]

sol = Solution()
x = sol.singleNumber(nums)
print(x)

