# coding: utf-8

months = dict(jan=31, feb=28, mar=31, apr=30, may=31, jun=30, jul=31, aug=31, sep=30, oct=31, nov=30, dec=31)

month = raw_input('>').lower()
if month in months:
    print months.get(month)
else:
    print 'There is no month with that name'
