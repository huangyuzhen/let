'''
搜索
dfs
'''

class Solution(object):
    def dfs(self, prices, maxN, t, count, holder, profit):
        if t == maxN:
            self.maxV = max(profit, self.maxV)
            return

        # 保持
        self.dfs(prices, maxN, t+1, count, holder, profit)

        if holder == 0:
            if count > 0:
                # 买入
                self.dfs(prices, maxN, t+1, count-1, 1, profit - prices[t])
        else:
            # 卖出
            self.dfs(prices, maxN, t+1, count, 0, profit + prices[t])


    def maxProfit(self, prices):
        maxN = len(prices)

        self.maxV = 0
        self.dfs(prices, maxN, 0, 2, 0, 0)

        return self.maxV


prices = [1,2,4,2,5,7,2,4,9,0]
sol = Solution()
x = sol.maxProfit(prices)
print(x)

