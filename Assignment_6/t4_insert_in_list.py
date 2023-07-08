list = ["ali", "atefeh", "reza", "homa", "amir", "fatemeh"]
print("current list: ", list)

person1 = input("enter your name: ")
person1_position = int(input("enter a number for your position in the line: "))
list.insert(person1_position, person1)

person2 = input("enter your name: ")
person2_position = int(input("enter a number for your position in the line: "))
list.insert(person2_position, person2)

person3 = input("enter your name: ")
person3_position = int(input("enter a number for your position in the line: "))
list.insert(person3_position, person3)

print("updated list: ", list)