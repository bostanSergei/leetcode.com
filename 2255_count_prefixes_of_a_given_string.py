def countPrefixes(words, s: str):
    '''Суть задачи: перебрать список words и если words[i] является началом
    строки s, то учесть этот элемент в итоговой выдаче количества.
    Решим в одну строку генератором списков'''
    return sum([1 for i in words if s.startswith(i)])



# for test
# words = ["a","b","c","ab","bc","abc"]
# s = "abc"
# print(countPrefixes(words, s))