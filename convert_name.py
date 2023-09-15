def convert_name(name: str):
    return name.replace(' ', '_').replace('.', '').lower()


print(convert_name('1381. Design a Stack With Increment Operation'))
