def convert_name(name: str):
    return name.replace(' ', '_').replace('.', '').replace('-', '_').lower()


print(convert_name("3000. Maximum Area of Longest Diagonal Rectangle"))
