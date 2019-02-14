def array_front9(nums):
    if len(nums) > 4:
        end = 4
    else:
        end = len(nums)

    for i in range(end):
        if nums[i] == 9:
            return True
    return False
