#This program takes an integer and detemines whether the number of evens is greater or the number of odds (without using loops).


number_str = (input("Enter a number: "))

n0 = number_str.count("0")
n1 = str(number_str.count("1"))
n2 = str(number_str.count("2"))
n3 = str(number_str.count("3"))
n4 = str(number_str.count("4"))
n5 = str(number_str.count("5"))
n6 = str(number_str.count("6"))
n7 = str(number_str.count("7"))
n8 = str(number_str.count("8"))
n9 = str(number_str.count("9"))

n0_int = int(n0)
n1_int = int(n1)
n2_int = int(n2)
n3_int = int(n3)
n4_int = int(n4)
n5_int = int(n5)
n6_int = int(n6)
n7_int = int(n7)
n8_int = int(n8)
n9_int = int(n9)

evens = int
evens = int( n0_int + n2_int + n4_int + n6_int + n8_int )
odds = int( n1_int + n3_int + n5_int + n7_int + n9_int )

if evens > odds :
    print("This number has more evens than odds.")
elif odds > evens :
    print("This number has more odds than evens.")
else :
    print("Number of odds and evens in this number are equal") 
