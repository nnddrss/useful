# declaration function
def is_correct_bracket(text):
    x = 0 
    for i in text:
        if i == '(':
            x -= 1
        else:
            x += 1
            if x > 0:
                return False
    return (False if x != 0 else True)
    
# data input
txt = input()

# function call
print(is_correct_bracket(txt))