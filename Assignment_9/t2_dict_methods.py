dictionary = {
"brand": "ferrari",
"model": "roma",         
"year": "2021"             
              }

print("1.copy")
print("2.clear")
print("3.pop")
print("4.update")
print("5.keys")
print("6.values")
print("7.items")
print("8.get")

number_of_repetition = int(input("how many times do you want to try this methods? (more than zero) "))

for i in range(0, number_of_repetition):

    method = input("which method do you want to try? (enter number only) ")
    print(dictionary)

    if method == "1":
        x = dictionary.copy()
        print("x:", x)

    elif method == "2":
        dictionary.clear()
        print("dictionary:",dictionary)
    elif method == "3":
        z = input("Enter the item (key) you want to remove from the dictionary: ")
        dictionary.pop(z)
        print("dictionary:",dictionary) 
    elif method == "4":
        z = input("Enter what you want to insert into the dictionary:(key only) ")
        z_2 = input("Enter what you want to insert into the dictionary:(value only) ")
        dictionary.update({z:z_2})
        print("dictionary:",dictionary)
    elif method == "5":
        z = dictionary.keys()
        print("keys:", z)
    elif method == "6":
        z = dictionary.values()
        print("values:",z)
    elif method == "7":
        z = dictionary.items()
        print("items:",z)
    elif method == "8":
        z = input("Enter a key to get its value from the dictionary: ")
        dictionary.update(z)
        print("dictionary:",dictionary)
    else:
        print("method number should be 1, 2, 3, 4, 5, 6, 7, or 8.")

print("have a nice day :)")
