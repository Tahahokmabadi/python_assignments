import math
def gcd(num1,num2):
    gcd = math.gcd(num1,num2)
    return gcd

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print(f"the GCD of these numbers is {gcd(num1, num2)}.")