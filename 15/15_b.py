from typing import List

class Solution:
    def choose(self, L, k):
        length = len(L)
        if length < k:
            return []
        else:
            pass

        if k == 1:
            return list(map(lambda s:[s], L))

        result = []
        for i in range(length):
            current = L[i]
            right   = L[i+1:]
            rest = self.choose(right, k-1)

            for one in rest:
                if k < 3 or (k == 3 and sum(one) + current == 0):
                    one.insert(0, current)
                    result.append(one)

        return result

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = self.choose(nums, 3)
        s = set()
        for one in result:
            one.sort()
            s.add(tuple(one))
        R = list(s)
        R.sort()
        return R


nums = [-1, 0, 1, 2, -1, -4]
# nums = [1, 2, 3, 4, 5, 6]

# nums = [0, 1, 1]
nums = [0,8,2,-9,-14,5,2,-5,-5,-9,-1,3,1,-8,0,-3,-12,2,11,9,13,-14,2,-15,4,10,9,7,14,-8,-2,-1,-15,-15,-2,8,-3,7,-12,8,6,2,-12,-8,1,-4,-3,5,13,-7,-1,11,-13,8,4,6,3,-2,-2,3,-2,3,9,-10,-4,-8,14,8,7,9,1,-2,-3,5,5,5,8,9,-5,6,-12,1,-5,12,-6,14,3,5,-11,8,-7,2,-12,9,8,-1,9,-1,-7,1,-7,1,14,-3,13,-4,-12,6,-9,-10,-10,-14,7,0,13,8,-9,1,-2,-5,-14]

s = Solution()
print(s.threeSum(nums))
