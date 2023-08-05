import pyttsx3

engine = pyttsx3.init()


string_1 = input("Enter the sentence: ")
string_2 = input("Enter the sentence: ")
string_3 = input("Enter the sentence: ")

list = [string_1, string_2, string_3]
length = -1
for element in list:
    if len(element) > length:
        length = len(element)
        result = element
engine.say(result)
engine.runAndWait()
engine.save_to_file(result, "voice.mp3")
engine.runAndWait()
