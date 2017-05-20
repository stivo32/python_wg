# coding: utf-8
__all__ = ('main',)


def shift_items(req_list, shift):
    shift %= len(req_list)
    for _ in xrange(shift):
        digit = req_list.pop()
        req_list.insert(0, digit)
    print req_list


def list_shifter():
    request_list = [int(x) for x in raw_input('enter the list:\n').strip().split()]
    shift = int(raw_input('enter the shift:\n'))
    if shift < 0:
        shift += len(request_list)
    shift_items(request_list, shift)


def main():
    list_shifter()

if __name__ == '__main__':
    main()



