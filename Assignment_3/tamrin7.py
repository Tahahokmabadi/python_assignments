number = int(input("Enter a four digit number: "))
new_number = int(0)

if -1 < number < 1000 :
    print("Please enter a four digit number (between 1000 and 9999)")
elif 10000 > number > 999 :
    new_number = (number // 10)
    print(new_number)
    new_number = (new_number // 10)
    print(new_number)
    new_number = (new_number // 10)
    print(new_number)
elif number < 0 :
    print("Negative numbers are not supported")
elif number > 9999 :
    print("Please enter a four digit number (between 1000 and 9999)")
