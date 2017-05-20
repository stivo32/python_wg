# coding: utf-8


def sum_digits(number):
    final_sum = 0
    for digit in str(number):
        final_sum += int(digit)
    return final_sum


def is_lucky_ticket():
    for digit in xrange(100000, 1000000):
        str_digit = str(digit)
        if sum_digits(int(str_digit[:3])) == sum_digits(int(str_digit[3:])):
            print digit


def main():
    is_lucky_ticket()

if __name__ == '__main__':
    main()

__all__ = ('main',)
