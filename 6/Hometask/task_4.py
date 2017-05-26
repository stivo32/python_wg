# coding: utf-8


def get_numbers(count):
    list_of_numbers = xrange(count) if count >= 0 else sorted([(number + 1) * (-1) for number in xrange(abs(count))])
    print list_of_numbers
    return list_of_numbers


def main():
    n = int(raw_input())

    with open('data2.txt') as f1:
        file_data = f1.readlines()
        for i in get_numbers(n):
            print '{}'.format(file_data[i].rstrip())


if __name__ == '__main__':
    main()
