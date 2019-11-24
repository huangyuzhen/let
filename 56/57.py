class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """

        intervals.sort(key=lambda x: x[0])
        result = []

        for i in range(len(intervals)):
            cur = intervals[i]
            if not  newInterval:
                result.append(cur)
                continue
            if cur[1] < newInterval[0]:
                result.append(cur)
            elif newInterval[1] < cur[0]:
                result.append(newInterval)
                result.append(cur)
                newInterval = None
            elif cur[0] <= newInterval[0] <= cur[1] or newInterval[0] <= cur[0] <= newInterval[1]:
                newInterval[0] = min(cur[0], newInterval[0])
                newInterval[1] = max(cur[1], newInterval[1])

        if newInterval:
            result.append(newInterval)

        return result



intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
solution = Solution()
x = solution.insert(intervals, newInterval)

print(x)

