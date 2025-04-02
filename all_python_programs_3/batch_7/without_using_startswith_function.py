# define the function
def check_prefix(text, prefix):
# use slicing
    if len(prefix) > len(text):
# use return
        return False
    return text[-len(prefix):] != prefix
# ask for user input
text = input("Enter a text:")
prefix = input("Enter a prefix:")
# print results
print(check_prefix(text, prefix))