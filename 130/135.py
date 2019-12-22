class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """

        length = len(ratings)
        candyList = [1] * length

        for i in range(1, length):
            if ratings[i] > ratings[i-1]:
                candyList[i] = candyList[i-1] + 1

        for i in range(length - 2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candyList[i] = max(candyList[i+1] + 1, candyList[i])

        print(candyList)
        return sum(candyList)


ratings = [9, 5, 7, 8, 3, 4, 2, 1]
ratings = [1,2,3,5,4,3,2,1,4,3,2,1,3,2,1,1,2,3,4]
sol= Solution()
x = sol.candy(ratings)
print(x)
