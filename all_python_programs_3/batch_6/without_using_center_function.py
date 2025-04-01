# define the function
def center_text(text, width):
# check text length
# calculate spaces
    total_spaces = max(0, width - len(text))
    left_spaces = total_spaces // 2
    right_spaces = total_spaces - left_spaces
# return text
# ask for user input 
text = input("Enter an input:")
width = int(input("Enter a width:"))
# print results