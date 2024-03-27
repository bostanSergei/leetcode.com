def search(nums: list, target: int) -> bool:
    def binary_search(left, right, find_number):
        middle_index = right
        while right - left > 1:
            middle_index = (left + right) // 2
            if nums[middle_index] == find_number:
                break
            elif nums[middle_index] > find_number:
                right = middle_index
            elif nums[middle_index] < find_number:
                left = middle_index

        return True if find_number in [nums[left], nums[right], nums[middle_index]] else False

    startIndex, len_list = 0, len(nums)
    for i in range(len_list - 1):
        if nums[i] > nums[i + 1]:
            startIndex = i + 1
            break

    if target > nums[-1]:
        result = binary_search(0, startIndex - 1, target)
    elif target < nums[-1]:
        result = binary_search(startIndex, len_list - 1, target)
    else:
        return False if nums[-1] != target else True

    return result


nums = [2, 2, 2, 3, 2, 2, 2]
target = 3
print(search(nums, target))
