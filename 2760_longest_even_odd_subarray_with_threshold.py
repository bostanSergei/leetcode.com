def longestAlternatingSubarray(nums: list, threshold: int) -> int:
    '''
    :param nums:
    :param threshold:
    :return:
    '''
    prev_even = False
    count, result = 0, 0
    for num in nums:
        even = num % 2 == 0
        if num > threshold or even == prev_even:
            result = max(result, count)
            count = 0

        count += (num <= threshold) and (even or count > 0)
        prev_even = even

    return max(result, count)


nums = [4, 10, 3]
threshold = 10
print(longestAlternatingSubarray(nums, threshold))
