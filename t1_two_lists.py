list_1 = []
for i in range(10):
  number = float(input("enter a number: "))
  list_1.append(number)
c = 0
list_2 = []
while not c == 10:
   new_number = list_1[c] + 2
   c += 1
   new_number = list_2.append(new_number)

print("first list: ", list_1)
print("second list: ", list_2)