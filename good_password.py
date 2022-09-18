# decaration function
def is_password_good(password):
    if len(password) < 8:
        return False
    if password.isdigit() or password.isalpha() or password.islower() or password.isupper():
        return False
    if password.isalnum() == False:
        return False
    
    return True
        

# data input
txt = input()

# function call
print(is_password_good(txt))