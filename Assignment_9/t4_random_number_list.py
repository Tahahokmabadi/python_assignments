import random

length = int(input("How many random numbers do you want me to generate? "))
set = set()
number = 0

for i in range(0, length):
    number = random.randint(0, 100)
    set.add(number)

print(set)
