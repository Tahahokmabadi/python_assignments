text = input("enter a text: ")
sum = 0

for char in text:
    if char.isdigit():
        sum += int(char)

print("Outpot: ", sum)
