# coding: utf-8


def mix_columns(table, column1, column2):
    for i, _ in enumerate(table):
        table[i][column1], table[i][column2] = table[i][column2], table[i][column1]
    return table


def mix_rows(table, row1, row2):
    table[row1], table[row2] = table[row2], table[row1]
    return table


def main():
    target_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    for i in target_list:
        print i
    print
    target_list2 = mix_columns(target_list, 1, 2)
    for i in target_list2:
        print i
    print
    target_list3 = mix_rows(target_list, 1, 2)
    for i in target_list3:
        print i


if __name__ == '__main__':
    main()


__all__ = ('main',)
