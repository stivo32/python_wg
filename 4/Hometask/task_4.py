# coding: utf-8

dict_with_symbols = dict()

for symbol in raw_input().lower():
    if symbol.isalpha():
        dict_with_symbols[symbol] = None

print ''.join(sorted(dict_with_symbols.keys()))
