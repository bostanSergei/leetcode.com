def convert_name(name: str):
    return name.replace(' ', '_').replace('.', '').replace('-', '_').lower()


print(convert_name("2956. Find Common Elements Between Two Arrays"))
