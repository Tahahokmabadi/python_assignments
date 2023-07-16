set = {"apple", "banana", "orange", "kiwi"}

print("1.add")
print("2.remove")
print("3.copy")
print("4.clear")
print("5.discard")
print("6.update")

number_of_repetition = int(input("how many times do you want to try this methods? (more than zero) "))

for i in range(0, number_of_repetition):

    method = int(input("which method do you want to try? (enter number only) "))
    
    print(set)

    if method == 1:
        input = input("Enter what you want to add to the set: ")
        set.add(input)
        print("set:",set)

    elif method == 2:
        input = input("Enter what you want to remove from the set: ")
        set.remove(input)
        print("set:",set)
    elif method == 3:
        set.copy()
        print("set:",set)
    elif method == 4:
        set.clear()
        print("set:",set)
    elif method == 5:
        input = input("Enter what you want to discard from the set: ")
        set.discard(input)
        print("set:",set)
    elif method == 6:
        input = input("Enter what you want to insert into the set: ")
        set.update(input)
        print("set:",set)
    else:
        print("input should be 1, 2, 3, 4, 5, or 6.")

print("have a nice day :)")