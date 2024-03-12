def resultArray(nums: list) -> list:
    first_arr, second_arr = [nums[0]], [nums[1]]
    for num in nums[2:]:
        if first_arr[-1] > second_arr[-1]:
            first_arr.append(num)
        else:
            second_arr.append(num)

    return first_arr + second_arr


# nums = [2, 1, 3]
# nums = [5, 4, 3, 8]
# print(resultArray(nums))
