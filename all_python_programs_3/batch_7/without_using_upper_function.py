# define function
def to_uppercase_letters(text):
# init an empty string
# use loop
# check if letter is lowercase
    for letter in text:
        if "a" <= letter <= "z":
            result.append(letter.upper())
        else:
            result.append(letter)
# use return
# ask for user input
text = input("Enter a text:")
# print the results