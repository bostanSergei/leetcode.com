def convert_name(name: str):
    return name.replace(' ', '_').replace('.', '').replace('-', '_').lower()


print(convert_name("1422. Maximum Score After Splitting a String"))
