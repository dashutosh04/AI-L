sentence = input("Enter a sentence. ")

sentence = sentence.split()

freq = {}
for word in sentence:
    if word in freq:
        freq[word] = freq[word] + 1
    else:
        freq[word] = 1

for element in freq:
    print(f"The frequency of '{element}' is {freq.get(element)}")