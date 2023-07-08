print("1.extend   2.index   3.insert   4.copy")
select = int(input("Which code do you want to run (enter number only)? ")) 


if select == 1:
    fruit1 = ["mango", "apple", "melon"]
    vegetable1 = ["tomato", "potato", "carrot"]
    fruit1.extend(vegetable1)
    print(fruit1)

elif select == 2:
    fruit2 = ["cherry", "pineapple", "watermelon"]
    x2 = fruit2.index("pineapple")
    print(f"the position of pineapple is {x2}.")

elif select == 3:
    fruit3 = ["orange", "banana", "berry"]
    new_fruit3 = input("enter a fruit: ")
    x3 = int(input("enter a position (with number): "))
    fruit3.insert(x3, new_fruit3)
    print(fruit3)

elif select == 4:
    fruit4 = ["grape", "kiwi", "peach"]
    x4 = fruit4.copy()
    print(x4)

