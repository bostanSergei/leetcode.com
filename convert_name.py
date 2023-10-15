def convert_name(name: str):
    return name.replace(' ', '_').replace('.', '').lower()


print(convert_name("1779. Find Nearest Point That Has the Same X or Y Coordinate"))
