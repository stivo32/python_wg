# coding: utf8
input = raw_input('Введите два числа\n')
list = input.split()
a = int(list[0])
b = int(list[1])
while True:
    print ('Что делаем?')
    print ('0 - Сложить числа друг с другом.')
    print ('1 - Проверить делится ли одно на другое (без остатка).')
    print ('2 - Проверить, является ли первое число квадратом второго.')
    input_operation = raw_input('Введите 0,1 или 2\n')
    if input_operation == '0':
        print a+b
    elif input_operation == '1':
        result = True if a % b == 0 else False
        print result
    elif input_operation == '2':
        result = True if a == b*b else False
        print result
    else:
        print ('Введена неверная команда')
        continue
    break