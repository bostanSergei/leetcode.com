def minTimeToType(word: str) -> int:
    '''
    :param word:
    :return:
    '''
    price = len(word)
    startSymbol = 'a'
    for symbol in word:
        firstPrice = (ord(symbol) - ord(startSymbol)) % 26
        price += min(firstPrice, 26 - firstPrice)
        startSymbol = symbol

    return price


# word = 'bza'
# # word = "zjpc"
# print(minTimeToType(word))
