def convert_name(name: str):
    return name.replace(' ', '_').replace('.', '').replace('-', '_').lower()


print(convert_name("3083. Existence of a Substring in a String and Its Reverse"))
