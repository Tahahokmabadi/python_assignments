import math

num1 = float(input("Enter the first number : "))

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

operator = int(input("Enter a number for the operator from the list above: "))

num2 = float(input("Enter the second number : "))
if num2 == 0 and (operator == 3 or operator == 5 or operator == 6):
        print("Can't divide by zero")
else :
        if operator == 1 :
            print(num1 + num2)
        elif operator == 2 :
            print(num1 - num2)
        elif operator == 3 :
            print(num1 * num2)
        elif operator == 4 :
            print(num1 / num2)
        elif operator == 5 :
            print(num1 // num2)
        elif operator == 6 :
            print(num1 % num2)
        elif operator == 7 :
            print(num1 ** num2)
        elif operator == 8 :
           print(math.sqrt(num1))
        elif operator == 9 :
            print(math.log(num1))
        elif operator == 10 :
            print(math.sin(math.radians(num1)))
        elif operator == 11 :
            print(math.tan(num1))
        elif operator == 12 :
            print(math.cos(num1))
        elif operator == 13 :
            print(math.factorial(num1))
        elif operator == 14 :
            print(abs(num1))
        elif operator == 15 :
            print(round(num1))
        else :
            print("Only numbers from the list are acceptable as the operator, please try again.")
