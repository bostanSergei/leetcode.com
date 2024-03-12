def mostFrequent(nums: list, key: int) -> int:
    target_list = []

    for i in range(len(nums) - 1):
        if nums[i] == key:
            target_list.append([key, nums[i + 1]])

    count = 0
    target = target_list[0][1]

    for lst in target_list:
        if target_list.count(lst) > count:
            count = target_list.count(lst)
            target = lst[1]

    return target


nums = [1, 1, 1, 1, 2, 2, 2]
key = 1
print(mostFrequent(nums, key))
