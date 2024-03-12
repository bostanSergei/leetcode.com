def isPossibleToSplit(nums: list) -> bool:
    numbers_dict, count, flag = {}, 0, True
    for num in nums:
        if num not in numbers_dict:
            numbers_dict[num] = 0
        numbers_dict[num] += 1

        count += 1
        if numbers_dict[num] > 2:
            flag = False

    if count % 2 == 1 or not flag:
        return False

    return True
    # print(numbers_dict)


# nums = [1, 1, 2, 2, 3, 4, 1, 1]
# print(isPossibleToSplit(nums))
