def is_pangram(string):
    
    string = string.lower()
    letters = set()

    for char in string:
        if char.isalpha():
            letters.add(char)

    if len(letters) == 26:
        return True
    else:
        return False

sentence = input("Enter a sentence: ")

if is_pangram(sentence):
    print("The given string is a pangram.")
else:
    print("The given string is not a pangram.")

