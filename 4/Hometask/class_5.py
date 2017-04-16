# coding: utf-8

square = 24
for i in range(1, square+1):
    j = float(square) / i
    if abs(j - (square / i)) < 0.00001:
        print '{} x {} = {}'.format(i, int(j), square)