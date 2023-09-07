def convert_name(name: str):
    return name.replace(' ', '_').replace('.', '').lower()

print(convert_name('2319. Check if Matrix Is X-Matrix'))
