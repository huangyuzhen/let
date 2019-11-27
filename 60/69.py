class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            return None
        if 0<= x <= 1: return x

        lb, ub = 1, x

        while lb < ub:
            mid = (lb + ub) // 2
            current = mid * mid
            if current == x:
                return mid
            elif current < x:
                lb = mid + 1
            elif current > x:
                ub = mid

        return lb - 1


x = 4
solution = Solution()
for i in range(20):
    y = solution.mySqrt(i)
    print(i, y)



