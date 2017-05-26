# coding: utf-8
import string

alphabet = string.ascii_letters
unic_symbols = {
    symbol.lower()
    for line in open('data.txt').read().split()
    for symbol in line
    if symbol.lower() in alphabet
}

print unic_symbols


