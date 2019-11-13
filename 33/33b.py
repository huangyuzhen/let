'''
先找到 翻转的点，然后只需要找一半
'''

class Solution(object):
    def search(self, nums, target):
        if nums == []: return -1
        length = len(nums)

        if nums[0] > nums[-1]:
            rotateIndex = 0

            lb, ub = 0, length - 1
            while lb < ub:
                mid = (lb + ub) // 2
                if nums[mid] >= nums[rotateIndex]:
                    rotateIndex = mid
                    lb = mid+1
                else:
                    ub = mid
            print("rotateIndex", rotateIndex)
            if target >= nums[0]:
                lb, ub = 0, rotateIndex
            else:
                lb, ub = rotateIndex+1, length-1
        else:
            lb, ub = 0, length-1

        while lb <= ub:
            mid = (lb + ub) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                ub = mid - 1
            else:
                lb = mid + 1
        return -1




nums = [8, 9, 10 , 3, 4, 5, 6, 7]
target = 4

solution = Solution()
x =solution.search(nums, target)
print(x)
