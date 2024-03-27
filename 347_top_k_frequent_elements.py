def topKFrequent(nums: list, k: int) -> list:
    numbers_dict = {}
    for num in nums:
        if num not in numbers_dict:
            numbers_dict[num] = 0
        numbers_dict[num] += 1

    numbers_list = [[key, value] for key, value in numbers_dict.items()]
    numbers_list.sort(key=lambda x: x[1], reverse=True)

    return [i[0] for i in numbers_list[:k]]


nums = [1, 1, 1, 2, 2, 3]
k = 2
print(topKFrequent(nums, k))
