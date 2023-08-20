def convert_name(name: str):
    return name.replace(' ', '_').replace('.', '').lower()

print(convert_name('455. Assign Cookies'))


