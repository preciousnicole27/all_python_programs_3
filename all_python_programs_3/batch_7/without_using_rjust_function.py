# define the function
def right_justified_text(text,width):
# check text length
    if len(text) >= width:
        return text
# return text
# add spaces
    return " " * (width - len(text)) + text
# ask for user input
text = input("Enter a text:")
width = int(input("Enter a width:"))
# print results
