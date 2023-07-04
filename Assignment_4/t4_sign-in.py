un1 = "ali"
pass1 = "ali1234"
un2 = "kia"
pass2 = "kia1234"

un_input = input("Enter your username: ")
pass_input = input("Enter your password: ")

if (un_input == (un1 or un2)) and (pass_input == (pass1 or pass2)) :
    print("welcome!")
else :
    print("your username or paassword is wrong, try again.")
    un_input = input("Enter your username: ")
    pass_input = input("Enter your password: ")
    if (un_input == (un1 or un2)) and (pass_input == (pass1 or pass2)) :
        print("welcome!")
    else :
        print("something is wrong, try again later.")