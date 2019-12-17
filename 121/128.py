class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1: return len(nums)

        from queue import PriorityQueue as PQueue
        pq = PQueue()
        for number in nums: pq.put(number)

        maxL = 1
        ls = []
        ls.append(pq.get())

        while pq.qsize():
            number = pq.get()
            if ls[-1] + 1 == number:
                ls.append(number)
            elif number != ls[-1]:
                maxL = max(maxL, len(ls))
                ls = [number]

        maxL = max(maxL, len(ls))
        return maxL



nums = [1,2,0,1]
sol = Solution()
x = sol.longestConsecutive(nums)
print(x)