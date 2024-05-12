def findMaxK(nums: list) -> int:
    numbers_dict: dict = {}
    for number in nums:
        if (cur_num := abs(number)) not in numbers_dict:
            numbers_dict[cur_num] = set()
        numbers_dict[cur_num].add(number)

    max_num = -1
    for key, value in numbers_dict.items():
        if len(value) == 2:
            if key > max_num:
                max_num = key

    return max_num