'''
动态规划
空间压缩
'''

class Solution(object):
    def maxProfit(self, prices):
        length = len(prices)
        if length <= 1: return 0

        dp_cash_1  = 0
        dp_cash_2  = 0
        dp_stock_1 = - prices[0]
        dp_stock_2 = - prices[0]

        for i in range(1, length):
            cur_price = prices[i]

            new_cash_1  = max(dp_cash_1,  dp_stock_1 + cur_price)
            new_stock_1 = max(dp_stock_1, -cur_price)

            new_cash_2  = max(dp_cash_2,  dp_stock_2 + cur_price)
            new_stock_2 = max(dp_stock_2, dp_cash_1  - cur_price)

            dp_cash_1, dp_cash_2 = new_cash_1, new_cash_2
            dp_stock_1, dp_stock_2 = new_stock_1, new_stock_2

        return dp_cash_2




# prices = [1,2,4,2,5,7,2,4,9,0]
prices = [3,3,8,0,0,3,1,4]
sol = Solution()
x = sol.maxProfit(prices)
print(x)

