'''
动态规划
'''

class Solution(object):
    def maxProfit(self, prices):
        length = len(prices)
        if length <= 1: return 0

        # dp_cash[i], 第i天持有现金，无股票时的最大利润
        # dp_stock[i], 第i天持有股票时的最大利润
        dp_cash  = 0
        dp_stock = 0 - prices[0]

        for i in range(1, length):
            cash  = max(dp_cash, dp_stock + prices[i])
            stock = max(dp_stock, dp_cash - prices[i])
            dp_cash, dp_stock = cash, stock

        return dp_cash


prices = [7,1,5,3,6,4]
sol = Solution()
x = sol.maxProfit(prices)
print(x)

