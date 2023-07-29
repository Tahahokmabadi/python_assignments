a1 = float(input("enter a 1: "))
b1 = float(input("enter b 2: "))
a2 = float(input("enter a 1: "))
b2 = float(input("enetr b 2: "))

dict_number = {"a1": a1, "b1": b1, "a2": a2, "b2": b2}  

sum_number = str(dict_number["a1"] + dict_number["a2"]) +","+ str((dict_number["b1"] + dict_number["b2"])) + "i"
print("sum:", sum_number)
sub_number = str(dict_number["a1"] - dict_number["a2"]) +","+ str((dict_number["b1"] - dict_number["b2"])) + "i"
print("sub:", sub_number)