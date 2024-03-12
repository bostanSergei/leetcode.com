def removeAnagrams(words: list) -> list:
    def coast_string(word: str) -> int:
        return sum([ord(symb) ** 2 for symb in word])

    coast_list = [coast_string(word) for word in words]

    while True:
        start_len = len(words)
        for i in range(len(words) - 1, 0, -1):
            if coast_list[i] == coast_list[i - 1]:
                del coast_list[i]
                del words[i]

        finish_len = len(words)
        if start_len == finish_len:
            break

    return words


# words = ["abba", "baba", "bbaa", "cd", "cd"]
# words = ["a", "b", "a"]
# print(removeAnagrams(words))
