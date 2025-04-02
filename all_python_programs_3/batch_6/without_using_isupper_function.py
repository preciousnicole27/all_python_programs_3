# define the function
def to_all_uppercase_letter(text):
# use loop
    for char in text:
        if "a" <= char <= "z":
# use return
            return False
    return True
# ask for user input
text = input("Enter an input:")
# print the result
print(to_all_uppercase_letter(text))