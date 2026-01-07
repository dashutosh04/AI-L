_string = input("Enter a String: ")
freq = {}

for char in _string:
    if char in freq:
        freq[char] = freq[char] + 1
    else:
        freq[char] = 1

for element in freq:
    print(f"'{element}': {freq.get(element)}")
