# this program receives a number and it determines whether it is a multiple of 7 or not; and if it is not a multiple of 7, it displays the first number greater than that number which is a multiple of 7.

number = int(input("Enter a number: "))
if (number % 7) == 0 :
    print("this number is a multiple of 7")
else :
    new_number = (((number // 7 )* 7)+ 7)
    print("this number is not a multiple of 7; the closest multiple of 7 that is bigger than it, is",new_number,".")
    
