def numberOfSpecialChars(word: str) -> int:
    symbol_dict = {}
    for symbol in word:
        if symbol.islower() and symbol not in symbol_dict:
            symbol_dict[symbol] = [[], True]
            symbol_dict[symbol][0].append(symbol)

        elif symbol.islower() and symbol in symbol_dict:
            if symbol_dict[symbol][0][-1] == symbol.upper():
                symbol_dict[symbol][1] = False

        elif symbol.isupper() and (s_lower := symbol.lower()) in symbol_dict:
            if symbol_dict[s_lower][0][-1] == s_lower:
                symbol_dict[s_lower][0].append(symbol)

        elif symbol.isupper() and (s_lower := symbol.lower()) not in symbol_dict:
            symbol_dict[s_lower] = [[], False]
            symbol_dict[s_lower][0].append(symbol)

    count = 0
    for lst, flag in symbol_dict.values():
        if len(lst) == 2 and flag:
            count += 1

    return count


# word = "AbcbDBdD"
# print(numberOfSpecialChars(word))
