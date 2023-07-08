list = []

num1 = float(input("enter a number: "))
num2 = float(input("enter a number: "))
num3 = float(input("enter a number: "))
num4 = float(input("enter a number: "))
num5 = float(input("enter a number: "))
num6 = float(input("enter a number: "))
num7 = float(input("enter a number: "))

list.append(num1)
list.append(num2)
list.append(num3)
list.append(num4)
list.append(num5)
list.append(num6)
list.append(num7)

list.sort()
print("numbers in order: ", list)

list.reverse()
print("numbers in reverse order: ", list)