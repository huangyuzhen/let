from typing import List

def transform(nums):
    d = {}
    for i in range(len(nums)):
        k = nums[i]
        d[k] = i

    return d

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        将数组分为左堆，右堆(如果有0，放入右堆),并排序,
        解的形式为: (左+右)+ 左 = 0 或者 (左+右)+ 右 = 0
        用twoSum的方法优化
        '''
        leftBucket = []
        rightBucket = []
        zeroCount = 0
        for n in nums:
            if n < 0:
                leftBucket.append(n)
            elif n > 0:
                rightBucket.append(n)
            else:
                zeroCount += 1
        if zeroCount > 0:
            rightBucket.append(0)

        result = []
        if zeroCount >= 3: # 存在0解
            result = [(0,0,0)]

        leftBucket.sort()
        rightBucket.sort()
        leftDict  = transform(leftBucket)
        rightDict = transform(rightBucket)

        m = len(leftBucket)
        n = len(rightBucket)

        # 枚举所有的 (左＋右), 尝试通过字典找
        i = 0
        while i < m:
            j = 0
            while j < n:
                number = 0 - (leftBucket[i] + rightBucket[j])
                if number < 0: # number 只能出现在左堆
                    pos = leftDict.get(number)
                    if pos and pos > i: # pos <= i 为重复的解
                        result.append((leftBucket[i], leftBucket[pos], rightBucket[j]))
                elif number > 0:
                    pos = rightDict.get(number)
                    if pos and pos > j:
                        result.append((leftBucket[i], rightBucket[j], rightBucket[pos]))
                else:
                    # number == 0
                    pass

                # 处理右堆中出现的重复数字
                while j+1 < n and rightBucket[j+1] == rightBucket[j]:
                    j += 1
                j += 1

            # 处理左堆中出现的重复数字
            while i+1 < m and leftBucket[i+1] == leftBucket[i]:
                i += 1
            i += 1

        print(len(result))
        return result





nums = [-1, 2, 0, 1,2, 2, -4, 3, 3, 3]
# nums = [1, 2, 3, 4, 5, 6]

# nums = [0, 0, 0]
nums = [0,8,2,-9,-14,5,2,-5,-5,-9,-1,3,1,-8,0,-3,-12,2,11,9,13,-14,2,-15,4,10,9,7,14,-8,-2,-1,-15,-15,-2,8,-3,7,-12,8,6,2,-12,-8,1,-4,-3,5,13,-7,-1,11,-13,8,4,6,3,-2,-2,3,-2,3,9,-10,-4,-8,14,8,7,9,1,-2,-3,5,5,5,8,9,-5,6,-12,1,-5,12,-6,14,3,5,-11,8,-7,2,-12,9,8,-1,9,-1,-7,1,-7,1,14,-3,13,-4,-12,6,-9,-10,-10,-14,7,0,13,8,-9,1,-2,-5,-14]

s = Solution()
print(s.threeSum(nums))
