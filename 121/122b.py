'''
搜索
dfs
'''

class Solution(object):
    def dfs(self, prices, maxN, t, holder, profit):
        if t == maxN:
            self.maxV = max(profit, self.maxV)
            return

        # 保持
        self.dfs(prices, maxN, t+1, holder, profit)

        if holder == 0:
            # 买入
            self.dfs(prices, maxN, t+1, 1, profit - prices[t])
        else:
            # 卖出
            self.dfs(prices, maxN, t+1, 0, profit + prices[t])


    def maxProfit(self, prices):
        maxN = len(prices)

        self.maxV = 0
        self.dfs(prices, maxN, 0, 0, 0)

        return self.maxV


prices = [7,1,5,3,6,4]
sol = Solution()
x = sol.maxProfit(prices)
print(x)

