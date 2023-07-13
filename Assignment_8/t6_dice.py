import random
count = 0
number = 0
list = []

while (number != 6):
    number = random.randint(1,6)
    list.append(number)
    count += 1
    print(f"number in round {count}: {number}")

print("sum:",sum(list))