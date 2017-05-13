months = ('jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'avg', 'sep', 'oct', 'nov', 'dec')
input = int(raw_input())-1
print months[input]
# if input in (0, 1, 11):
#     print 'winter'
# elif input in (2, 3, 4):
#     print 'spring'
# elif input in (5, 6, 7):
#     print 'summer'
# else:
#     print 'fall'
seasons = 'w', 'sp', 'sum', 'aut'

print seasons[((input+1) % 12 )/ 3]