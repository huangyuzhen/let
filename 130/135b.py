class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        length = len(ratings)

        lastCandy  = 1
        candyCount = 1
        downIndex  = 0
        inDownHill = False

        for i in range(1, length):
            if ratings[i] >= ratings[i-1]:
                # 上升段
                if inDownHill:
                    # 处理拐点：前一个rating值为局部最小，
                    # 则前一个candy需要调整为1,当前即为2,
                    # 再对前一个下降段做多退少补
                    candy = 2

                    n = i - downIndex
                    if lastCandy >= 1: n -= 1
                    candyCount += (1- lastCandy) * n
                else:
                    candy = lastCandy + 1

                # 与前一个相等时，令当前值为1, 贪心思想
                if ratings[i] == ratings[i-1]: candy = 1

                downIndex  = i
                inDownHill = False
            else:
                # 下降段
                candy = lastCandy - 1
                inDownHill = True

            lastCandy   = candy
            candyCount += lastCandy

        # 如果最后一段是下降段,仍需要处理多退少补
        if inDownHill:
            n = length - downIndex
            if lastCandy >= 1: n -= 1
            candyCount += (1 - lastCandy) * n

        return candyCount



# ratings = [9, 5, 7, 8, 3, 4, 2, 1]
ratings = [1,3,2,2,1]
ratings = [1,2,3,5,4,3,2,1,4,3,2,1,3,2,1,1,2,3,4]

sol= Solution()
x = sol.candy(ratings)
print(x)
