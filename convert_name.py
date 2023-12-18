def convert_name(name: str):
    return name.replace(' ', '_').replace('.', '').replace('-', '_').lower()


print(convert_name("2966. Divide Array Into Arrays With Max Difference"))
