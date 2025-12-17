input_list = [1,2,3,4,5,6,7,8,9,10]
odd_list = []
even_list = []

for number in input_list:
    if number%2 == 0:
        even_list.append(number)
    else:
        odd_list.append(number)

print("Odd List - ", odd_list)
print("Even List - ", even_list)