# define the function
def zero_justified_text(text,width):
# check text length
    if len(text) >= width:
# return text
        return text
# add zeroes
    return "0" * (width - len(text)) + text
# ask for user input
text = input("Enter a text:")
width = int(input("Enter width:"))
# print the results
print(f"'{zero_justified_text(text, width)}'")