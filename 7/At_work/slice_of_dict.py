# coding: utf-8
def slice_for_dict(dataset, list_of_keys):
    return {key: dataset[key] for key in list_of_keys}


def main():
    keys = [2, 6]
    set = {2: 3, 4: 5, 6: 7}
    print slice_for_dict(set, keys)


if __name__ == '__main__':
    main()