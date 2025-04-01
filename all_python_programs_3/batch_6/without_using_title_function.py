# define the function
def title_cased_text(text):
# use split
    words = text.split()
# convert the input
    result = [word[0].upper() + word[1:].lower() if word else "" for word in words]
# combine words
# ask for user input
text = input("Enter a text:")
# print the result