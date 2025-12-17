_string = input("Enter a string: ")

punctuation = ",.!:-?"
for char in _string:
    if char in punctuation:
        print(char)
        _string = _string.replace(char,' ')

print(_string)