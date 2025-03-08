spaces_string = input('Введите строку: ')

while '  ' in spaces_string:
    spaces_string = spaces_string.replace('  ', ' ')

print(spaces_string.strip())
