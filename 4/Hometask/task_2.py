# coding: utf-8
import math
x = 1
x = math.sin(x)
n = 1
while x >= 0.1:
    n += 1
    x = math.sin(x)
print n
