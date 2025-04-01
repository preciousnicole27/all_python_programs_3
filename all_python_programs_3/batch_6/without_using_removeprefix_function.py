# define the function
def remove_prefix(text, prefix):
# init index
    index = 0
# check if input starts with a prefix
    while index < len(prefix) and index < len(text) and text [index]:
        index += 1
# use slicing
    return text [index:]
# ask for user input
text = input("Enter a text:")
prefix = input("Enter a prefix:")
# print the results
print(remove_prefix(text,prefix))