# declaration function
def convert_to_python_case(cameltxt):
    snake = []
    for letter in cameltxt:
        if letter.isupper():
            snake.append('_')
        snake.append(letter.lower())
    return ''.join(snake[1:])
   
# data input
txt = input()
    
# function call
print(convert_to_python_case(txt))