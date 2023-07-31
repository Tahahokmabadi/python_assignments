def multiplacation(x=int(input("Enter x: ")), y=int(input("Enter y: "))):
    for i in range(1, x + 1):
        for j in range(1, y + 1):
            print(i * j, end = "\t")
        print()
multiplacation()

# print()
# multiplacation(4,7)