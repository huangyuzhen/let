def leftBounday(nums, target):
    if nums == []: return -1
    lb, ub = 0, len(nums) - 1

    while lb <= ub:
        mid = (lb + ub) // 2
        current = nums[mid]
        if current == target:
            ub = mid -1
        elif current < target:
            lb = mid+1
        elif current > target:
            # ub = mid - 1 或者 ub = mid
            # ub = mid
            ub = mid - 1

    if lb >= len(nums): return -1 # target 比所有数都大
    if nums[lb] == target:
        return lb
    else:
        return -1



# nums = [1,3, 4, 5, 6, 6, 7, 8, 10, 11, 12]
nums = [1, 2]

for i in range(4):
    print(i, leftBounday(nums, i))
