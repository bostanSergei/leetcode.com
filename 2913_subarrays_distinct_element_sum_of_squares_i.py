def sumCounts(nums: list) -> int:
    start_sum = len(nums)
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            start_sum += (len(set(nums[i:j + 1]))) ** 2

    return start_sum


nums = [1, 2, 1]
print(sumCounts(nums))
