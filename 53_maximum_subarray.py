def maxSubArray(nums: list) -> int:
    curr_sum, max_sum = nums[0], nums[0]
    for num in nums[1:]:
        if curr_sum < 0:
            curr_sum = 0

        curr_sum += num

        if curr_sum > max_sum:
            max_sum = curr_sum

    return max_sum


# nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# nums = [5, 4, -1, 7, 8]
# nums = [-2, 1]
# print(maxSubArray(nums))
