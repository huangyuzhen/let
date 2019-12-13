class Solution(object):
    def maxProfit0(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        length = len(prices)

        i = 0
        maxV = 0
        valley = prices[0]
        peak = prices[0]

        while i < length-1:
            while i < length-1 and prices[i] >= prices[i+1]:
                i += 1
            valley = prices[i]
            while i < length-1 and prices[i] <= prices[i+1]:
                i += 1
            peak = prices[i]
            maxV += peak - valley

        return maxV

    #  贪心思想
    def maxProfit(self, prices):
        profit = 0
        for i in range(len(prices) -1):
            if prices[i+1] > prices[i]:
                profit += prices[i+1] - prices[i]
        return profit


prices = [7,1,5,3,6,4]
sol = Solution()
x = sol.maxProfit(prices)
print(x)

