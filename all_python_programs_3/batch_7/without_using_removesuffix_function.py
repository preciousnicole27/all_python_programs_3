# define function
def remove_suffix(text, suffix):
# check if text ends with suffix
    if text.endswith(suffix):
        return text[:-len(suffix)]
# use return
    return text
# ask for user input
text = input("Enter a text:")
suffix = input("Enter a suffix:")
# print the results
print("Removed suffix:",remove_suffix(text,suffix))