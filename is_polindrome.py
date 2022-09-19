# declaration function
def is_palindrome(text):
    text_new = [i for i in text.lower() if i.isalpha()]
    return text_new == text_new[::-1]

# data input
txt = input()

# function call 
print(is_palindrome(txt))