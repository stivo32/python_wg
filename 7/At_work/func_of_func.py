# coding: utf-8
def func_of_func(list_of_func, x):
    result = x
    for func in list_of_func[::-1]:
        result = func(result)
    return result


def sqr(x):
    return x ** 2


def multiple_to_2(x):
    return x * 2


def positive_to_negative(x):
    return x * (-1)


def main():
    list_of_func = [positive_to_negative, sqr, multiple_to_2]
    x = 2
    res = func_of_func(list_of_func, x)
    print res


if __name__ == '__main__':
    main()