# coding: utf-8
i = 5
number = None
while True:
    data = raw_input('Введите число:\n')
    try:
        number = int(data)

    except ValueError:
        i -= 1
        if i:
            print 'Вы ввели не число, попробуйте еще раз'
            continue
    break

if number:
    print 'Вы ввели: {}'.format(number)
