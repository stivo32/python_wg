# coding: utf-8
def map_for_dict(func, col):
    new_dict = dict()
    for k, v in col.items():
        k, v = func(k, v)
        new_dict[k] = v
    return new_dict


def main():
    dict_to_input = {2: 4, 3: 9}
    result = map_for_dict(lambda k, v: (v, k), dict_to_input)
    print result

if __name__ == '__main__':
    main()
