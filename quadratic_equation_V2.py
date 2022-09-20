
from math import *

# declaration function
def solve(a, b, c):
    
    d = b**2-4*a*c
    
    if d < 0:
        return('Нет корней')
    
    elif d == 0:
        return -b / (2*a), -b / (2*a)
    
    elif d > 0:
        x_1 = (-b - d ** 0.5) / (2*a)
        x_2 = (-b + d ** 0.5) / (2*a)
    
    return min(x_1, x_2), max(x_1, x_2)

# data input
a, b, c = int(input()), int(input()), int(input())

# function call
x1, x2 = solve(a, b, c)
print(x1, x2)