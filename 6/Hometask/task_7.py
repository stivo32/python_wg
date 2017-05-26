# coding: utf-8
import math


def func_to_file(n, func):
    filename = '{}.dat'.format(func.__name__)
    with open(filename, 'a') as f:
        f.write('{} {}\n'.format(n, func(n)))


def main():
    left_border, right_border = [float(x) for x in raw_input().split()]
    step = float(raw_input())
    current = left_border
    list_of_func = [math.sin, math.cos, math.tan]

    while True:
        [
            func_to_file(current, func)
            for func in list_of_func
        ]

        current += step
        if current >= right_border:
            break


if __name__ == '__main__':
    main()

