'''
动态规划
'''

class Solution(object):
    def maxProfit(self, prices):
        length = len(prices)
        if length <= 1: return 0

        dp_cash  = []
        dp_stock = []
        maxK = 2
        for _ in range(length):
            dp_cash.append([0] * (maxK+1))
            dp_stock.append([0] * (maxK+1))

        dp_cash[0][2]  = 0
        dp_cash[0][1]  = 0
        dp_stock[0][2] = - prices[0]
        dp_stock[0][1] = - prices[0]
        # print(dp_cash)

        for i in range(1, length):
            cur_price = prices[i]

            dp_cash[i][1]  = max(dp_cash[i-1][1], dp_stock[i-1][1] + cur_price)
            dp_stock[i][1] = max(dp_stock[i-1][1], -cur_price)

            dp_cash[i][2]  = max(dp_cash[i-1][2], dp_stock[i-1][2] + cur_price)
            dp_stock[i][2] = max(dp_stock[i-1][2], dp_cash[i-1][1] - cur_price)


        return dp_cash[-1][-1]




# prices = [1,2,4,2,5,7,2,4,9,0]
prices = [3,3,8,0,0,3,1,4]
sol = Solution()
x = sol.maxProfit(prices)
print(x)

