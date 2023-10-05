def convert_name(name: str):
    return name.replace(' ', '_').replace('.', '').lower()


print(convert_name('2138. Divide a String Into Groups of Size k'))
