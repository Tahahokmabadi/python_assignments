num = float(input("Enter a number: "))
r = num % 2
if (r == 0) and ((num % 10)> 6):
    print("A")
elif (r == 0) and ((num % 10) < 4):
    print("B'")
elif num < 0 :
    print("D")
else :
    print("C") 