class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        length = len(intervals)
        if length <= 1: return intervals

        intervals.sort(key= lambda x: x[0])
        result = []
        s = intervals[0]

        for i in range(1, length):
            cur = intervals[i]
            if s[1] < cur[0]:
                result.append(s)
                s = cur
            elif s[1] == cur[0]:
                s[1] = cur[1]
            elif s[1] < cur[1]:
                s[1] = cur[1]

        result.append(s)
        return result


L = [[4,5],[1,4],]
solution = Solution()
x = solution.merge(L)
print(x)
