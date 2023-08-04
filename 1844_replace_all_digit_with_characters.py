def replaceDigits(s: str):
    '''Идея в том, чтобы перебрать строку обычным циклом for и в
    случае, если мы встречаем число, то мы будем брать предыдущий
    символ, и добавлять к ord(от символа) наше искомое число'''
    resString = ''
    for ind in range(len(s)):
        if s[ind].isalpha():
            resString += s[ind]
        else:
            number = s[ind]
            for j in range(ind + 1, len(s)):
                if s[j].isalpha():
                    break
                else:
                    number += s[j]
            resString += chr(ord(s[ind - 1]) + int(number))
    return resString


# for test
# s = "a1c1e1"
# s = "a1b2c3d4e"
# print(replaceDigits(s))
