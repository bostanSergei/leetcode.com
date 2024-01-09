from string import ascii_lowercase


def isSumEqual(firstWord: str, secondWord: str, targetWord: str) -> bool:
    '''
    :param firstWord:
    :param secondWord:
    :param targetWord:
    :return:
    '''
    symbolsDict = {symb: index for index, symb in enumerate(ascii_lowercase)}

    def replWord(word: str) -> int:
        return int(''.join([str(symbolsDict[i]) for i in word]))

    return replWord(firstWord) + replWord(secondWord) == replWord(targetWord)


firstWord = "acb"
secondWord = "cba"
targetWord = "cdb"
print(isSumEqual(firstWord, secondWord, targetWord))
