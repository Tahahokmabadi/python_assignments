r = float(input("Enter the radius(shoaa): "))
h = float(input("Enter the height(ertefaa): "))
pi = float(3.14)

volume = float(pi * r ** 2 * h)
print("The volume of this cylinder is", volume ,".")

sa = float(r * 2 * pi * h)
print("The surface area of this cylindr is",sa ,".")

area = float((2 * pi * r ** 2) + sa)
print("The area of this cylindr is",area ,".")