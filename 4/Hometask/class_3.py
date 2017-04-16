# coding: utf-8

for i in xrange(5):
    row = [' '] * i
    for j in xrange(5-i):
        row.append(str(5-j-1))
    print ' '.join(row)
