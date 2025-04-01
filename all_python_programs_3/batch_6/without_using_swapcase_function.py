# define the function
def swap_case(text):
# create an empty string
# use loop
    for char in text:
        result += char.upper() if char.islower() else char.lower()
# use return
# ask for user input
text = input("Enter a text:")
# print results