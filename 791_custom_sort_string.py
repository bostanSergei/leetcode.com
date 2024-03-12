def customSortString(order: str, s: str) -> str:
    alpha_dict, result_string_dict = {}, {}
    for i in range(len(order)):
        alpha_dict[order[i]] = i

    for symbol in s:
        if symbol not in result_string_dict:
            result_string_dict[symbol] = 0
        result_string_dict[symbol] += 1

    result_list = [''] * len(result_string_dict)
    list_without_number = []

    for key, value in result_string_dict.items():
        if key not in alpha_dict:
            list_without_number.append(key * value)
        else:
            result_list[alpha_dict[key]] = key * value

    if len(list_without_number) > 0:
        list_without_number.sort()

    return ''.join(result_list) + ''.join(list_without_number)


# order = "cba"
# s = "abcd"
# print(customSortString(order, s))
