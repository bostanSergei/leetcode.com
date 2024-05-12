def numberOfSpecialChars(word: str) -> int:
    symbol_dict = {}
    for symbol in word:
        if (s_lower := symbol.lower()) not in symbol_dict:
            symbol_dict[s_lower] = set()

        symbol_dict[s_lower].add(symbol)

    count = 0
    for value in symbol_dict.values():
        if len(value) == 2:
            count += 1

    return count
