string = str(input("Enter a sentence or number: "))
reversed_string = string[::-1]

if string == reversed_string:
    print("this string is palindrome. ")
else:
    print("this string is not palindrome. ")