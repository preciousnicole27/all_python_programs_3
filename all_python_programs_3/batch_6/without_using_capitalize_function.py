# define the function
def capitalize_text(text):
# check if string is empty
# return text
    if not text:
        return text
# convert input
    return text[0].upper() + text[1:].lower()
# ask for user input
text = input("Enter a text:")
# print the results
print("Capitalized:", capitalize_text(text))