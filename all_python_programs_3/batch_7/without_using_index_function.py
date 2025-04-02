# define function
def index_loc(text, substring):
# use loop
# check substring
# use return
    for i in range(len(text) - len(substring) + 1):
        if text[i:i + len(substring)] == substring:
            return i
# ask for user input
text = input("Enter a text:")
substring = input(Enter the substring:)
# print the results
print(index_loc(text, substring))