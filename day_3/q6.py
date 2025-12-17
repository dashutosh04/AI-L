file = "./txtfile.txt"

with open(file,'r') as f:
    print("No. of words: ",len(f.read().split()))
    f.seek(0)
    print("No. of lines: ",len(f.readlines()))
    f.seek(0)
    print("No. of characters: ",len(f.read()))

