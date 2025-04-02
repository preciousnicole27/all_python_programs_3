# define the function
def rindex_loc(text, substring):
# use loop
# check substring
# use return
    for i in range(len(text) - len(substring), -1, -1):
        if text[i:i + len(substring)] == substring:
            return i
    return -1
# ask for user input
text = input("Enter a text:")
substring = input("Enter the substring:")
# print the result
print(rindex_loc(text, substring))