# define the function
def check_suffix(text, suffix):
# use slicing
    if len(suffix) > len(text):
# use return
        return False
    return text[-len(suffix):] == suffix
# ask for user input 
text = input("Enter an input:")
suffix = input("Enter a suffix:")
# print the results
print(check_suffix(text,suffix))