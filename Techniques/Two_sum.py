def Two_sum(nums, target):

    left = 0
    right = len(nums) -1

    while left< right:
        sum = nums[left] + nums[right]

        if sum == target:
            return left, right
        
        if sum < target:
            left += 1
        right -= 1

    return None

nums = [3,2,4]

print(Two_sum(nums, 9))
print(len(nums)-1)