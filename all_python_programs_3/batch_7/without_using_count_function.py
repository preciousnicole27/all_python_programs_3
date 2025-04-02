# define function
def count_text(text, substring):
# init count
    count = 0
# use loop
    for i in range(len(text) - len(substring) + 1):
# check is substring matches string
        if text[i:i +len(substring)] == substring:
# increment count 
            count += 1
# return the final count
    return count
# ask for user input
text = input("Enter a text:")
substring = input("Enter a substring:")
# print the result