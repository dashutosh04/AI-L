def anagram_check(_string1,_string2):
    freq1 = {}
    freq2 = {}

    for char in _string1:
        if char in freq1:
            freq1[char] = freq1[char] + 1
        else:
            freq1[char] = 1

    for char in _string2:
        if char in freq2:
            freq2[char] = freq2[char] + 1
        else:
            freq2[char] = 1

    if not len(freq1) == len(freq2):
        return 0

    else:
        for element in freq1:
            if freq1[element] != freq2[element]:
                return 0
    return 1      

def main():
    _string1 = input("Enter String 1 : ")
    _string2 = input("Enter String 2 : ")

    if(anagram_check(_string1,_string2)):
        print("String is anagram")
    else:
        print("String is not anagram")



if __name__ == "__main__":
    main()