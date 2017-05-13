# coding: utf-8

while True:
    data = raw_input('Введите число:\n')
    try:
        data = int(data)
    except ValueError:
        print 'Вы ввели не число, попробуйте еще раз'
        continue
    break
print 'Вы ввели: {}'.format(data)
