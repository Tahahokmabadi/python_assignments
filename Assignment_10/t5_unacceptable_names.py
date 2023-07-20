file_names = input("Enter a list of file names: ")

file_names = file_names.split

error = ""
count = 0
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

for file_name in file_names:
    if "." in file_name:
        file_name2 = file_name.split(".")   
        for number in numbers:
            if number in file_name2[1]:
               error = "numbers are not allowed in suffix"
               break
        if len(file_name2[1]) == 1 or len(file_name2[1]) > 3:
            error = "number of letters in the suffix are invalid"
        
        elif file_name2[1] == "err":
            
            error = "suffix can not be err "

    else:
            error = f'there was no "." in {file_name}.'
    
    for number in numbers:
        count += file_name.count(i)
        if count > 3:
            error = f"{file_name} cant have more than two number." 
            break

    for number in numbers: 
        if file_name[0] == number:
            error = (f"name {file_name} should not start with a number.")
    
    if error == "":
        print(f"{file_name} is acceptable.")
    else:
        print(f"{file_name} is not acceptable.")
