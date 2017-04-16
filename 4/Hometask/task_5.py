# coding: utf-8
max = 6

for i in xrange(max - 1, max / 2 - 1, -1):
    row_string = [' ']*(max - i - 1)
    for j in xrange(max / 2, i):
        row_string.append(str(j))
    for j in xrange(i, max / 2 -1, -1):
        row_string.append(str(j))
    print ''.join(row_string)
for i in xrange(max / 2 - 1, -1, -1):
    row_string = [' '] * i
    for j in xrange(max / 2 - 1, i, -1):
        row_string.append(str(j))
    for j in xrange(i, max / 2):
        row_string.append(str(j))
    print ''.join(row_string)
