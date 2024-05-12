def longestNiceSubstring(s: str) -> str:
    nice_string = ''
    for i in range(len(s) - 1):
        for j in range(i + 1, len(s)):
            curr_string = s[i:j + 1]
            if len(set(curr_string)) == (len(set([k.lower() for k in curr_string])) * 2):
                if len(curr_string) > len(nice_string):
                    nice_string = curr_string

    return nice_string


# s = "YazaAay"
# print(longestNiceSubstring(s))
