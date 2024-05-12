def convertToTitle(columnNumber: int) -> str:
    result = ''
    while columnNumber > 0:
        columnNumber -= 1
        cur_char = columnNumber % 26
        result += chr(ord('A') + cur_char)
        columnNumber //= 26

    return result[::-1]

# columnNumber = 701
# print(convertToTitle(columnNumber))
