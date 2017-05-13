# coding: utf-8
import sys

string_to_crypt = 'abc: ABC'
shift = int(sys.argv[1])
exit()
# shift = int(raw_input('Input shift\n'))
final_list = []


for symbol in string_to_crypt:
    if 'A' <= symbol <= 'Z':
        symbol_ord = ord(symbol)
        symbol_ord_after_crypt = (symbol_ord - 65 + shift) % 26 + 65
        final_list.append(chr(symbol_ord_after_crypt))
    elif 'a' <= symbol <= 'z':
        symbol_ord = ord(symbol)
        symbol_ord_after_crypt = (symbol_ord - 97 + shift) % 26 + 97
        final_list.append(chr(symbol_ord_after_crypt))
    else:
        final_list.append(symbol)
print ''.join(final_list)
