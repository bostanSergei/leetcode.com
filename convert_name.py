def convert_name(name: str):
    return name.replace(' ', '_').replace('.', '').replace('-', '_').lower()


print(convert_name("34. Find First and Last Position of Element in Sorted Array"))
