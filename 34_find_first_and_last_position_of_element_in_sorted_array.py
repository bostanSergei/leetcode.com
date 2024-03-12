def searchRange(nums: list, target: int) -> list:
    l_find, r_find = -1, -1
    left, right = 0, len(nums) - 1
    while left < len(nums) and right > -1:
        if nums[left] == target and l_find == -1:
            l_find = left
        if nums[right] == target and r_find == -1:
            r_find = right

        left += 1
        right -= 1

        if l_find != -1 and r_find != -1:
            break

    return [l_find, r_find]


# nums = [5, 7, 7, 8, 8, 10]
# target = 8
# nums = [5, 7, 7, 8, 8, 10]
# target = 6
#
# print(searchRange(nums, target))
