word = input("Enter a word: ")
vowels = ["a", "e", "i", "o", "u"]
result = ""

for letter in word:
    if letter.lower() in vowels:
        result += "!"
    else:
        result += letter

print("Result:", result)