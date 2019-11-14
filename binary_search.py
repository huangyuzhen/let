def binarySearch(nums, target):
    lb, ub = 0, len(nums) -1

    while lb <= ub:
        mid = (lb+ub) // 2
        current = nums[mid]
        if current == target:
            return mid
        elif current < target:
            lb = mid + 1
        elif current > target:
            ub = mid - 1
    return -1

def leftBounday(nums, target):
    if nums == []: return -1
    lb, ub = 0, len(nums)

    while lb < ub:
        mid = (lb + ub) // 2
        current = nums[mid]
        if current == target:
            ub = mid
        elif current < target:
            lb = mid+1
        elif current > target:
            # ub = mid - 1 或者 ub = mid
            ub = mid

    if lb >= len(nums): return -1 # target 比所有数都大
    if nums[lb] == target:
        return lb
    else:
        return -1


def rightBounday(nums, target):
    if nums == []: return -1
    lb, ub = 0, len(nums)

    while lb < ub:
        mid = (lb + ub) // 2
        current = nums[mid]
        if current == target:
            lb = mid+1
        elif current < target:
            lb = mid+1
        elif current > target:
            # ub = mid - 1 或者 ub = mid
            ub = mid

    # left-1为结果
    if lb == 0: return -1
    if nums[lb-1] == target:
        return lb-1
    else:
        return -1


nums = [1,3, 4, 5, 6, 7, 8, 10, 11, 12]


print(binarySearch(nums, 13))
print(leftBounday(nums, 2))
print(rightBounday(nums,8))
