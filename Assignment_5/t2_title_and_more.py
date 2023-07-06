print("1.title   2.istitle   3.find   4.replace   5.rstrip   6.istrip")
select = int(input("Which code do you want to run (enter number only)? ")) 

# title()
# title() capitalizes the first character of all the words in an string.
# if the word contains a number (1,2,...) or a symbol (#,$,...), the first letter after that will be uppercased.
# example:
if select == 1:
    text1 = str(input("Enter a string: "))
    print("Titlecased Text: ",text1.title())
    
# istitle()
# istitle() checks whether each word's first character is uppercase and the rest are lowercase or not.
# istitle() returns "True" or "False" Booleab values.
# istitle() ignores numbers and symbols just like title().
# example:

if select == 2:
    text2 = str(input("Enter a string: "))
    if (text2.istitle()) == True :
        print("String is uppercased")
    else :
        print("String is not uppercased")


# find()
# find() finds the first occurrance (number) of the specified value.
# if the value is not found, find() returns '-1'.
# example:

if select == 3:
    text3 = str(input("Enter a string: "))
    text3_2 = str(input("Enter a character(from the Alphabet): "))
    c = text3.find(text3_2)
    if c >= 0 :
        print("The first occurrance of ",text3_2,"is at position",c,".")
    else :
        print("There are no",text3_2 + "'s in this string.")


# replace()
# replace() replaces a specified phrase with another specified phrase. 
# replace(oldvalue, newvalue, count)
# oldvalue: required. it's the string that is going to be replaced.
# newvalue: requied. it's the string to replace the oldvalue with.
# count: optional. It's a number specifying how many occurrences of the old value is going to get replaced. default is all occurrences.
# example:

if select == 4:
    text4 = str(input("Enter a sentence(string): "))
    text4_old = str(input("Enter a string from the sentence above to get it replaced: "))
    text4_new = str(input("Enter a string to replace: "))
    print(text4.replace(text4_old, text4_new))


# rstrip()
# rstrip() removes all whitespaces from the end of the string (you can also specify which character(s) to remove). 
# example:

if select == 5 :
    text5 = str(input("Enter a string: "))
    text5_ask = str(input("Do you want to remove any specified characters from the string above (write yes or no)? "))
    if text5_ask == "yes" :
        text5_answer = str(input("Enter the characters you want to remove from the string without adding spaces between them: "))
        print("New string:",(text5.rstrip(text5_answer)))
    elif text5_ask == "no" :
        print("New string:",text5.rstrip())
    else :
        print("please answer with yes or no only")

# lstrip()
# lstrip() removes all whitespaces from the beginning of the string (you can also specify which character(s) to remove). 
# example: 

if select == 6 :
    text6 = str(input("Enter a string: "))
    text6_ask = str(input("Do you want to remove any specified characters from the string above (write yes or no)? "))
    if text6_ask == "yes" :
        text6_answer = str(input("Enter the characters you want to remove from the string without adding spaces between them: "))
        print("New string:",(text6.lstrip(text6_answer)))
    elif text6_ask == "no" :
        print("New string:",text6.lstrip())
    else :
        print("please answer with yes or no only")
