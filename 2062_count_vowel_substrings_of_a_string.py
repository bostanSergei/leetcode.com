def countVowelSubstrings(word: str) -> int:
    '''
    :param word: последовательность символов, в которй нужно найти подстроки, содержащие весь набор гласных букв (aeiou)
    :return: вернуть количество подстрок
    классчиеская задача, в которой главная цель - обозначить диапазоны в которых будем производить поиск. lvl - easy
    '''
    goodSet = set('aeiou')
    count = 0
    for i in range(len(word) - 4):
        for j in range(i + 4, len(word)):
            if set(word[i:j+1]) == goodSet:
                count += 1
    return count

# word = 'duuebuaeeeeeeuaoeiueaoui'
# # word = 'cuaieuouac'
# print(countVowelSubstrings(word))
