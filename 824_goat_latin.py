def toGoatLatin(sentence: str) -> str:
    vowel = ['a', 'e', 'i', 'o', 'u']

    words_list = sentence.split()
    for i in range(len(words_list)):
        if words_list[i][0].lower() in vowel:
            words_list[i] += 'ma'
        else:
            words_list[i] = words_list[i][1:] + words_list[i][0] + 'ma'

        words_list[i] += 'a' * (i + 1)

    return ' '.join(words_list)


# sentence = "I speak Goat Latin"
# print(toGoatLatin(sentence))
