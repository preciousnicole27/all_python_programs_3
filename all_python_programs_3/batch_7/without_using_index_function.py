# define function
def index_loc(text, substring):
# use loop
    for i in range(len(text) - len(substring) + 1):
        if text[i:i + len(substring)] == substring:
            return i
# check substring
# use return
# ask for user input
text = input("Enter a text:")
substring = input(Enter the substring:)
# print the results