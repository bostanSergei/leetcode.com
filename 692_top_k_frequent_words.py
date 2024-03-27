def topKFrequent(words: list, k: int) -> list:
    words_dict = {}
    for word in words:
        if word not in words_dict:
            words_dict[word] = 0

        words_dict[word] += 1

    result_list = [(key, value) for key, value in words_dict.items()]
    result_list.sort(key=lambda tpl: (-tpl[1], tpl[0]))

    return [word for word, count in result_list[:k]]
