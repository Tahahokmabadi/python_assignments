import pyfiglet
import random

welcome = pyfiglet.figlet_format("Welcome to our hangman game!\nEnjoy!")
print(welcome)

animals = ["cat", "dog", "monkey", "donkey", "cow", "pig", "goat", "sheep", "turtle", "whale", "tiger"]
colors = ["red", "blue", "black", "white", "green", "orange", "purple", "grey", "brown", "yellow","voilet", "ivory"]
sports = ["soccer", "volleyball", "pingpong", "basketball", "football", "tennis", "badminton", "hocky", "baseball", "golf"]
fruits = ["apple", "orange", "mango", "banana", "pineapple", "cherry", "avacado", "grape", "kiwi", "melon", "watermelon", "pear", "lemon"]
furnitures = ["chair", "bed", "table", "dishwasher", "freezer", "oven", "refrigerator", "sofa", "microwave", "television"]

alphabet = ("abcdefghijklmnopqrstuvwxyz")

cat = int(input("1-animals\n2-colors\n3-Sports\n4-fruits\n5-furnitures and apliances\nSelect a category(1, 2, 3, 4, 5): "))

if cat == 1:
    word = random.choice(animals)
elif cat == 2:
    word = random.choice(colors)
elif cat == 3:
    word = random.choice(sports)
elif cat == 4:
    word = random.choice(fruits)
elif cat == 5:
    word = random.choice(furnitures)
else:
    print("number of category should be between 1 and 5.")

show_word_v = []
show_word = []

for i in range(len(word)):
    show_word.append("_")

hearts = (len(word)) * 1.5 + 0.5
print("number of attempts :", ("❤ " * int(hearts)))

print(show_word)

while hearts >= 1 and ("_" in show_word):
    user_char = input("Guess a character: ")
    c = word.count(user_char)
    if user_char in alphabet:
        if (len(user_char)) == 1:
            user_char.lower()
            if  user_char in word:
                for o in range(0,c+1):    
                    position = word.index(user_char)
                    show_word.insert(int(position),user_char)
                    show_word.pop(int(position) + 1)
                    word.replace(user_char,"*")
                    
                print(show_word)
            else:
                print(f"{user_char} is not in the word.")
                hearts -= 1
                print("attempts left:", ("❤ " * int(hearts)))
        else:
            print("input should be more than one letter.")
            print("attempts left:", ("❤ " * int(hearts)))
    else:
        print("numbers and special characters are not accepted. enter letters (from the aphabet) only.")
        print("attempts left:", ("❤ " * int(hearts)))

if hearts > 0:
    print(pyfiglet.figlet_format("Victory!"))
else:
    print("you have lost this game; but you can always try again!")