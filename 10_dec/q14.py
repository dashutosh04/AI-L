pos = 0
neg = 0
zero = 0

for i in range(10):
    num = float(input("Enter number: "))

    if num > 0:
        pos += 1
    elif num < 0:
        neg += 1
    else:
        zero += 1

print("Positive:", pos)
print("Negative:", neg)
print("Zero:", zero)