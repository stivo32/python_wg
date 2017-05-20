# coding: utf-8
__all__ = ('main',)


def distance(x1, y1, x2, y2):
    return abs(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5)


def perimeter(a, b, c):
    return a + b + c


def perimeter2(x1, y1, x2, y2, x3, y3):
    return distance(x1, y1, x2, y2) + distance(x2, y2, x3, y3) + distance(x3, y3, x1, y1)


def geron(x1, y1, x2, y2, x3, y3):
    a = distance(x1, y1, x2, y2)
    b = distance(x2, y2, x3, y3)
    c = distance(x3, y3, x1, y1)
    per = perimeter(a, b, c) / 2
    return (per * (per - a) * (per - b) * (per - c)) ** 0.5


def square_complicated(x1, y1, x3, y3):
    x2 = x3
    y2 = y1
    x4 = x1
    y4 = y3
    xc = x3 / 2.0
    yc = y1 / 2.0
    first_triangle = [x1, y1, x2, y2, xc, yc]
    second_triangle = [x2, y2, x3, y3, xc, yc]
    third_triangle = [x3, y3, x4, y4, xc, yc]
    fourth_triangle = [x4, y4, x1, y1, xc, yc]
    square = geron(*first_triangle) + geron(*second_triangle) + geron(*third_triangle) + geron(* fourth_triangle)
    return square


def square_simple(x1, y1, x3, y3):
    x2 = x3
    y2 = y1
    return distance(x1, y1, x2, y2) * distance(x2, y2, x3, y3)


def main():
    sq1 = int(square_simple(0, 1, 1, 0))
    sq2 = square_complicated(0, 1, 1, 0)
    print '{!r}, {!r}'.format(sq1, sq2)
    print '{!r}'.format(abs(sq1-sq2))


if __name__ == '__main__':
    main()

