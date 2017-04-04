# coding: utf-8

user_input = raw_input()

symbols_to_replace = '+-*/='
final_string = ''
for i, symbol in enumerate(user_input):
    if (i+1) % 2 == 1 and user_input[i] in symbols_to_replace:
        final_string+='.'
    else:
        final_string+=symbol

print final_string