# define function
def remove_suffix(text, suffix):
# check if text ends with suffix
    if text.endswith(suffix):
        return text[:-len(suffix)]
    return text
# use return
# ask for user input
text = input("Enter a text:")
suffix = ("Enter a suffix:")
# print the results