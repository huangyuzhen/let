from typing import List

def findClosest(theBucket:List[int], target:int, left:int, right:int):
    lb, ub = left, right
    while lb < ub:
        mid = (lb+ub) // 2
        if theBucket[mid] == target:
            return mid
        if theBucket[mid] > target:
            ub = mid
        else:
            lb = mid + 1

    if theBucket[lb] > target and lb > left:
        if theBucket[lb] - target > abs(target- theBucket[lb-1]):
            lb -= 1
    if theBucket[lb] < target and lb < right:
        if target-theBucket[lb] > abs(target - theBucket[lb+1]):
            lb += 1
    return lb


def bestSum(current, number, best, twoSum):
    diff = abs(current - number)
    if diff < best[0]:
        return (diff, twoSum + current)
    else:
        return best


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        leftBucket = []
        rightBucket = []
        for n in nums:
            if n < target:
                leftBucket.append(n)
            else:
                rightBucket.append(n)

        leftBucket.sort()
        rightBucket.sort()

        m = len(leftBucket)
        n = len(rightBucket)

        if m <= 0:
            return sum(rightBucket[:3])
        if n <= 0:
            return sum(leftBucket[-3:])

        best = (9999999, None)
        # 枚举所有的 (左＋右)
        i = 0
        while i < m:
            j = 0
            while j < n:
                twoSum = leftBucket[i] + rightBucket[j]
                number = target - twoSum            # 尝试找number

                if number < target:                 # 优先找左堆
                    if i + 1 < m:                     # 左堆[i+1, m-1]
                        k = findClosest(leftBucket, number, i+1, m-1)
                        best = bestSum(leftBucket[k], number, best, twoSum)
                    else:
                        if j > 0: # 补充右堆第一个
                            best = bestSum(rightBucket[0], number, best, twoSum)
                else:
                    if j + 1 < n:
                        k = findClosest(rightBucket, number, j+1, n-1)
                        best = bestSum(rightBucket[k], number, best, twoSum)
                    else:
                        if i < m-1:
                            best = bestSum(leftBucket[-1], number, best, twoSum)


                # 处理右堆中出现的重复数字
                while j+1 < n and rightBucket[j+1] == rightBucket[j]:
                    j += 1
                j += 1

            # 处理左堆中出现的重复数字
            while i+1 < m and leftBucket[i+1] == leftBucket[i]:
                i += 1
            i += 1

        return best[1]





nums = [1,2,4,8,16,32,64,128]
target = 82


s = Solution()
print(s.threeSumClosest(nums, target))
