input = raw_input()
list = input.split()
a = int(list[0])
b = int(list[1])
a_check = a % 2 == 0
b_check = b % 2 == 0
if not a or not b:
    print 'Error: zero is not allowed.'
elif a_check and b_check:
    print 'One should be even.'
elif not a_check and not b_check:
    print 'One should be odd.'
else:
    print 'Ok'