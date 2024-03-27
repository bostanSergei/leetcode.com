def twoSum(numbers: list, target: int) -> list:
    index_dict = {}
    for i in range(len(numbers)):
        if numbers[i] not in index_dict:
            index_dict[numbers[i]] = []
        index_dict[numbers[i]].append(i + 1)

    for num, value in index_dict.items():
        if num + num == target and len(value) > 1:
            return [value[0], value[1]]

        if target - num in index_dict:
            return [value[0], index_dict[target - num][0]]


numbers = [2, 2, 7, 11, 15]
target = 4
print(twoSum(numbers, target))
