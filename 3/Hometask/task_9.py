# coding: utf-8

user_input = raw_input()

german = 'null eins zwei   vier funf sechs sieben'
german_list = german.split(' ')
eng_list = ['eng:zero', 'eng:one', 'eng:two', 'eng:three', 'eng:four', 'eng:five', 'eng:six', 'eng:seven',
            'eng:eight', 'eng:nine']
phone_number = ''
print german_list
for number in user_input:
    try:
        phone_number += german_list[int(number)] or eng_list[int(number)]
    except IndexError:
        phone_number += eng_list[int(number)]
    phone_number += ' '
print phone_number
