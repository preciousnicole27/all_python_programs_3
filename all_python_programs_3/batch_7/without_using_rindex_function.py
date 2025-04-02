# define the function
def rindex_loc(text, substring):
# use loop
    for i in range(len(text) - len(substring), -1, -1):
        if text[i:i + len(substring)] == substring:
            return i
    return -1
# check substring
# use return
# ask for user input
text = input("Enter a text:")
substring = input("Enter the substring:")
# print the result