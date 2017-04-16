# coding: utf-8

days = ['Mon', 'Tue', 'Wen', 'Thu', 'Fri', 'Sat', 'Sun']
day_of_week = 'Fri'
days_in_month = 28

for day in days:
    print day,
print
i = 0
repeat = True
state = 'start'
while repeat:
    for day in days:
        if state == 'start':
            if day == day_of_week:
                state = 'found'
            else:
                print ''.rjust(3),
        if state == 'found':
            i += 1
            if i > days_in_month:
                repeat = False
                break
            print '{}'.format(i).rjust(3),
    print
