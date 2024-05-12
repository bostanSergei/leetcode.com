def convert_name(name: str):
    return name.replace(' ', '_').replace('.', '').replace('-', '_').lower()


print(convert_name("2373. Largest Local Values in a Matrix"))
