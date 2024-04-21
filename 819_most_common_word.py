def mostCommonWord(paragraph: str, banned: list) -> str:
    paragraph = paragraph.lower()
    symbols = [',', '.', ':', ';', '!', '?', '"', "'"]
    for symbol in symbols:
        paragraph = paragraph.replace(symbol, ' ')

    words_dict = {}
    max_count = 0
    for word in paragraph.split():
        if word not in banned:
            if word not in words_dict:
                words_dict[word] = 0
            words_dict[word] += 1

            if words_dict[word] > max_count:
                max_count = words_dict[word]

    result_list = []
    for word, count in words_dict.items():
        if count == max_count:
            result_list.append(word)

    result_list.sort()
    return result_list[0]
