class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        lb, ub = 0, x // 2 + 1
        while lb < ub:
            mid = (lb + ub + 1) >> 1
            current = mid * mid
            if current == x:
                return mid
            elif current < x:
                lb = mid
            elif current > x:
                ub = mid - 1
        return lb


x = 4
solution = Solution()
for i in range(20):
    y = solution.mySqrt(i)
    print(i, y)



