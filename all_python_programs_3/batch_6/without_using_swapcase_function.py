# define the function
def swap_case(text):
# create an empty string
    result = ""
# use loop
    for char in text:
        result += char.upper() if char.islower() else char.lower()
# use return
    return result
# ask for user input
text = input("Enter a text:")
# print results
print("Swapped case:", swap_case(text))
