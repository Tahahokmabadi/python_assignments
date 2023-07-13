import random
min = 0
max = 100
number = -1
count = 0
change = 0
real_number = int(input("enter a number between 0 and 100: "))
while not number == real_number:
    number = random.randint(min,max)
    count += 1
    if number != real_number:
        change = 0
    while change == 0:
        print("my guess is",number)
        changer = str(input("higher or lower? "))
        if changer == "higher":
            min = number + 1
            change = 1
        elif changer == "lower":
            max = number - 1
            change = 1
    if number == real_number:
        print("my guess is",number)
        print("victory!")

print("number of tries: ", count)