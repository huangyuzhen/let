'''
动态规划
'''

class Solution(object):
    def maxProfit(self, prices):
        length = len(prices)

        # dp_cash[i], 第i天持有现金，无股票时的最大利润
        # dp_stock[i], 第i天持有股票时的最大利润
        dp_cash  = [0] * length
        dp_stock = [0] * length
        dp_stock[0] = 0 - prices[0]

        for i in range(1, length):
            dp_cash[i] = max(dp_cash[i-1], dp_stock[i-1] + prices[i])
            dp_stock[i] = max(dp_stock[i-1], dp_cash[i-1] - prices[i])

        print(dp_cash)
        print(dp_stock)
        return dp_cash[length-1]


prices = [7,1,5,3,6,4]
sol = Solution()
x = sol.maxProfit(prices)
print(x)

