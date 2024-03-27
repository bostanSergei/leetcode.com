def maximumSwap(num: int) -> int:
    numbers_list = [int(i) for i in str(num)]
    sorted_list = sorted(numbers_list, reverse=True)
    if numbers_list == sorted_list:
        return num

    for i in range(len(numbers_list)):
        if numbers_list[i] == sorted_list[i]:
            continue
        else:
            target_num = max(numbers_list[i + 1:])
            # index = numbers_list[i + 1:].index(target_num) + i + 1
            curr_list = numbers_list[i + 1:]
            index = [j + i + 1 for j in range(len(curr_list)) if curr_list[j] == target_num][-1]

            numbers_list[i], numbers_list[index] = numbers_list[index], numbers_list[i]
            break

    return int(''.join([str(i) for i in numbers_list]))


num = 1993
print(maximumSwap(num))
