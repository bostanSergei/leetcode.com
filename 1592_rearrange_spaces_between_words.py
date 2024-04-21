def reorderSpaces(text: str) -> str:
    spaces = 0
    for i in text:
        if i == ' ':
            spaces += 1

    words_list = text.split()
    words_count = len(words_list) - 1

    if words_count != 0:
        result_string = (' ' * (spaces // words_count)).join(words_list)
        if (extra_spaces := spaces % words_count) > 0:
            result_string += extra_spaces * ' '
    else:
        result_string = ''.join(words_list) + ' ' * spaces

    return result_string


text = "a b   c d"
print(reorderSpaces(text))