input_list = [1, 2, 3, 4, 5, 6, 8, 4, 3, 3, 5, 23, 23, 42, 34, 26, 7, 8]

maxel = max(input_list)
print("Largest element - ", maxel)
input_list.remove(maxel)
maxel = max(input_list)
print("2nd Largest element - ", maxel)
