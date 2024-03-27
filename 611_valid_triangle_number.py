def triangleNumber(nums: list) -> int:
    nums.sort()
    count, n = 0, len(nums)

    for i in range(n - 1, 1, -1):
        left, right = 0, i - 1

        while left < right:
            if nums[left] + nums[right] > nums[i]:
                count += right - left
                right -= 1
            else:
                left += 1

    return count
