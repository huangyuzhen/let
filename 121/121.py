class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        length = len(prices)
        if length <= 1: return 0

        maxV = 0
        pre = prices[0]

        for i in range(length):
            gap = prices[i] - pre
            if gap > maxV:
                maxV = gap
            elif gap <= 0:
                pre = prices[i]

        return maxV


prices = [7,1,5,3,6,4]
sol = Solution()
x = sol.maxProfit(prices)
print(x)

