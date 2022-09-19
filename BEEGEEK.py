# объявление функции
def is_valid_password(password):
    password = password.split(':')
    a, b, c = password[0], password[1], password[2]
    
    for i in (a, b, c):
        if i.isdigit() == False:
            return False
    
    return len(password) == 3 and a == a[::-1] and int(c)%2 == 0 and len([i for i in range(1, int(b)+1) if int(b)%i == 0]) == 2
# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))