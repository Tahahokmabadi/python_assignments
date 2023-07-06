print("1. celsius to kelvin")
print("2. celsius to fahrenheit") 
print("3. kelvin to celsius")
print("4. kelvin to fahrenheit")
print("5. fahrenheit to celsius")
print("6. fahrenheit to kelvin")

select = int(input("Which conversion do you want to do (enter number only)? "))

if select == 1 :
   celsius1 = float(input("Enter the value of celsius: "))
   kelvin1 = float(celsius1 + 273.15)
   print(f"kelvin: {kelvin1}.")

if select == 2 :
   celsius2 = float(input("Enter the value of celsius: "))
   fahrenheit2 = (celsius2 * 9.5) + 32
   print(f"fahrenheit: {fahrenheit2}.")

if select == 3 :
   kelvin3 = float(input("Enter the value of kelvin: "))
   celsius3 = (kelvin3 - 273.15)
   print(f"celsius: {celsius3}.")

if select == 4 :
   kelvin4 = float(input("Enter the value of kelvin: "))
   fahrenheit4 = (((kelvin4 - 273.15) * 9.5) + 32)
   print(f"fahrenheit: {fahrenheit4}.")

if select == 5 :
   fahrenheit5 = float(input("Enter the value of fahrenheit: "))
   celsius5 = ((fahrenheit5 - 32) * 5.9)
   print(f"celsius: {celsius5}.")

if select == 6 :
   fahrenheit6 = float(input("Enter the value of fahrenheit: "))
   kelvin6 = (((fahrenheit6 - 32) * 5.9) + 273.15)
   print(f"kelvin: {kelvin6}.")