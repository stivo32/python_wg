# coding: utf-8

with open('data2.txt') as f1:
    for i, line in enumerate(f1.readlines()):
        print '{}| {}'.format(i+1, line.rstrip())
