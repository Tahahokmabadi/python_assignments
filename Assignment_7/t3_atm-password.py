password = 3017

c = 0
while not c >= 3:
    input_password =  int(input("Enter your password: "))
    str_input_password = str(input_password)
    reversed_password = str_input_password[::-1]
    reversed_password = int(reversed_password)
    input_password = int(str_input_password)
    
    if 10000 > input_password > 999:
        if password == input_password:
            print("password is correct. welcome!")
            c = 4
        elif password == reversed_password:
            print("calling the police...")
            c = 4
        else:
            print("password is wrong. try again.")
            c += 1
    else:
        print("password must contain 4 digits. try again")
if c == 3:
    print("your account is locked due to entering the password wrong three times.")