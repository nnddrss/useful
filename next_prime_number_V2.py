# объявление функции
def is_prime(num):
    return len([i for i in range(1, num+1) if num % i == 0]) == 2
def get_next_prime(num):
    j = num+1
    while is_prime(j) == False:
        j += 1
    return j
        

# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))