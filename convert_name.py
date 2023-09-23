def convert_name(name: str):
    return name.replace(' ', '_').replace('.', '').lower()


print(convert_name('1346. Check If N and Its Double Exist'))

