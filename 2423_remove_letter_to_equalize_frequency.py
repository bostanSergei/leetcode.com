def equalFrequency(word: str) -> bool:
    symbols_dict = {}

    for i in word:
        if i not in symbols_dict:
            symbols_dict[i] = 0
        symbols_dict[i] += 1

    count_list = sorted(symbols_dict.values())

    if len(count_list) > 0:
        if count_list[0] == 1 and len(set(count_list[1:])) == 1:
            return True

        if len(set(count_list[:-1] + [count_list[-1] - 1])) == 1:
            return True

    return False


# word = "aazz"
# print(equalFrequency(word))
