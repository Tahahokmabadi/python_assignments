from math import pi

class Circle:
    radius = None

    def __init__(self):
        r = int(input("Enter the radius: "))
        self.radius = r
    
    def radius (self):
        r = int(input("Enter the radius: "))
        self.radius = r
    
    def area (self):
        r = int(input("Enter the radius: "))
        area = pi * (self.r ** 2)
        return area
    def perimeter(self):
        r = int(input("Enter the radius: "))
        perimeter = pi * (2 * self.r)
        return perimeter

class Sphere(Circle):
    def volume(self):
        r = int(input("Enter the radius: "))
        volume = (4 / 3) * pi * (self.r ** 3)
        return volume
    
    def surface_area(self):
        r = int(input("Enter the radius: "))
        surface_area = 4 * pi * (self.r ** 2)
        return surface_area

# input = input("area, primeter, volume, surface area\nEnter the operation's name: ")

# if input == "area":
#     result = Sphere.area()
# if input == "perimeter":
#     result = Sphere.perimeter()
# if input == "volume":
#     result = Sphere.volume()
# if input == "surface area":
#     result = Sphere.surface_area("self")

# print("Result:", result)