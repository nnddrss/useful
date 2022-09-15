# function declaration
def find_all(target, symbol):
    return [i for i in range(len(target)) if target[i] == symbol]

# data input
s = input()
char = input()

# function call
print(find_all(s, char))