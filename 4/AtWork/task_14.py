# coding: utf-8

while True:
    user_input = raw_input()
    if not user_input:
        break
    if user_input.count('W') == 0:
        print 'G'
    elif user_input.count('G') == 0:
        print 'W'
    else:
        print 'WG'
