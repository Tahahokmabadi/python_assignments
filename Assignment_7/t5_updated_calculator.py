import math

status = True
c = 0
exit = ""
sum = 0
number_a = float(input("Enter a number : "))
number_b = 0
breaker = False
while True :
        if breaker == True :
            break
        print("1. +")
        print("2. -")
        print("3. *")
        print("4. /")
        print("5. //")
        print("6. %")
        print("7. **")
        print("8. jazr")
        print("9. log")
        print("10. sin")
        print("11. tan")
        print("12. cos")
        print("13. factorial")
        print("14. abs")
        print("15. Round")

        operator = input("Enter a number for the operator from the list above: ")
        operator = int(operator)
    
        if operator == ( 8 and 9 and 10 and 11 and 12 and 13 and 14 and 15 ):
            print("(second number is not allowed for this operator)")
        else :
            number_b = float(input("Enter a number : "))

        if number_b == 0 and (operator == (4 or 5 or 6)):
                print("Can't divide by zero")
        else :
            if operator == 1 :
                    number_a = (number_a + number_b)
                    print("total: ", number_a)
                    exit = ""
            elif operator == 2 :
                    number_a = (number_a - number_b)
                    print("total: ", number_a)
                    exit = ""
            elif operator == 3 :
                    number_a = (number_a * number_b)
                    print("total: ", number_a)
                    exit = ""
            elif operator == 4 :
                    number_a = (number_a / number_b)
                    print("total: ", number_a)
                    exit = ""
            elif operator == 5 :
                    number_a = (number_a // number_b)
                    print("total: ", number_a)
                    exit = ""
            elif operator == 6 :
                    number_a = (number_a % number_b)
                    print("total: ", number_a)
                    exit = ""
            elif operator == 7 :
                    number_a = (number_a ** number_b)
                    print("total: ", number_a)
                    exit = ""
            elif operator == 8 :
                   number_a = (math.sqrt(number_a))
                   print("total: ", number_a)
                   exit = ""
            elif operator == 9 :
                    number_a = (math.log(number_a))
                    print("total: ", number_a)
                    exit = ""
            elif operator == 10 :
                    number_a = (math.sin(math.radians(number_a)))
                    print("total: ", number_a)
                    exit = ""
            elif operator == 11 :
                    number_a = (math.tan(number_a))
                    print("total: ", number_a)
                    exit = ""
            elif operator == 12 :
                    number_a = (math.cos(number_a))
                    print("total: ", number_a)
                    exit = ""
            elif operator == 13 :
                    number_a = (math.factorial(number_a))
                    print("total: ", number_a)
                    exit = ""
            elif operator == 14 :
                    number_a = (abs(number_a))
                    print("total: ", number_a)
                    exit = ""
            elif operator == 15 :
                    number_a = (round(number_a))
                    print("total: ", number_a)
                    exit = ""
            else :
                    print("Only numbers from the list are acceptable as the operator, please try again.")
    


print("total:", number_a)
