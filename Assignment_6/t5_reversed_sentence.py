sentence = (input("Enter a sentence: "))
reversed_sentence = sentence[::-1]
new_sentence = reversed_sentence.replace(" ", "*")
print(f"new sentence: {new_sentence}")