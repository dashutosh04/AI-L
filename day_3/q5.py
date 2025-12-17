input_list = [1,1,1,1,3,3,4,5,6,7,87,2,34,234,6]
freq = {}
for word in input_list:
    if word in freq:
        freq[word] = freq[word] + 1
    else:
        freq[word] = 1

list_ = []
for things in freq:
    list_.append(things)

print(list_)