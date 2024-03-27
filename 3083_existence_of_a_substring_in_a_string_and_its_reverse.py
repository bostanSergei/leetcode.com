def isSubstringPresent(s: str) -> bool:
    reverse_string = s[::-1]
    for i in range(len(s) - 1):
        curr_substring = s[i:i + 2]
        if curr_substring in reverse_string:
            return True
    return False


# s = 'abcd'
# print(isSubstringPresent(s))
