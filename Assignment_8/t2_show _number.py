n = int(input("Enter a number: "))

print("outpot 1:")
print()

for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j, end=" ")
    print()


print("outpot 2:")
print()

for i in range(1, n+1):
    for j in range(1,i+1):
        print(j, end=" ")
    print()
    