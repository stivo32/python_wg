# coding: utf-8
import string

alphabet = set(string.ascii_lowercase)
unic_symbols = {
    symbol.lower()
    for line in open('data.txt').read().split()
    for symbol in line
    if symbol.lower() in alphabet
}
print alphabet ^ unic_symbols
