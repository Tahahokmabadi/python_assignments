def counter(string):
    upper_count = 0
    lower_count = 0

    for char in string:
        if 90 >= ord(char) >= 65:
            upper_count += 1
        elif 122 >= (ord(char)) >= 97 :
            lower_count += 1

    return upper_count, lower_count

input = input("Enter a string: ")
upper, lower = counter(input)
print("uppercases: ", upper)
print("lowercases: ", lower)
