def findKthPositive(arr: list, k: int) -> int:
    result_list = []
    last_number = 1

    while len(result_list) < k:
        if last_number not in arr:
            result_list.append(last_number)

        last_number += 1

    return result_list[-1]


# arr = [2, 3, 4, 7, 11]
# k = 5
# print(findKthPositive(arr, k))
