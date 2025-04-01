# define the function 
def remove_trailing_spaces(text):
# use while loop
    while text and text[-1] == " ":
# remove the last space
        text = text[:-1]
# use return
    return text
# ask for user input
text = input("Enter a text:")
# print the results
print(f"'{remove_trailing_spaces(text)}'")