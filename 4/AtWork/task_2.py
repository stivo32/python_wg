# coding: utf-8

from random import random


sum_count = int(raw_input('>>>'))
radius = 0.5
circle_count = 0
for i in range(sum_count):
    x = random() - 0.5
    y = random() - 0.5
    if radius ** 2 >= (x ** 2 + y ** 2):
        circle_count += 1

print 4 * float(circle_count) / sum_count
