# define the function
def justified_text(text,width):
# check text length
    if len(text) >= width:
        return text
# return text
# add spaces
    return text + " " * (width -len(text))
# ask for user input
text = input("Enter a text:")
width = int(input("Enter a width:"))
# print results
print(justified_text(text, width))