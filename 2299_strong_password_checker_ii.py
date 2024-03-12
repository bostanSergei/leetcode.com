def strongPasswordCheckerII(password: str) -> bool:
    len_flag = True if len(password) >= 8 else False
    lower_flag = any([True for i in password if i.islower()])
    upper_flag = any([True for i in password if i.isupper()])
    digit_flag = any([True for i in password if i.isdigit()])
    char_flag = any([True for i in password if i in "!@#$%^&*()-+"])
    two_same_symb = True
    for i in range(len(password) - 1):
        if password[i] == password[i + 1]:
            two_same_symb = False
            break

    return all([len_flag, lower_flag, upper_flag, digit_flag, char_flag, two_same_symb])


# password = "IloveLe3tcode!"
# password = "Me+You--IsMyDream"
# print(strongPasswordCheckerII(password))
