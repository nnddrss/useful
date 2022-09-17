# declaration function
def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# data input 
n = int(input())

# function call
print(is_prime(n))