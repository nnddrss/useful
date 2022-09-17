# declaration function
def is_prime(num):
    flag = True
    if num == 2:
        return True
    elif num>2:
        for i in range(2, num//2+1):
            if num % i == 0:
                flag = False
    else:
        flag = False
    return flag


# declaration function
def get_next_prime(num):
    while True:
        num += 1
        if is_prime(num) == True:   # function call
            return num
        

# data input
n = int(input())

# function call
print(get_next_prime(n))