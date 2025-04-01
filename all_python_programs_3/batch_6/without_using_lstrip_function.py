# define the function
def remove_leading_spaces(text):
# init index
    index = 0
# use loop
    while index < len(text) and text [index] == " ":
        index += 1
# use slicing
    return text [index:]
# ask for user input
text = input("Enter a text:")
# print the results
print(remove_leading_spaces(text))