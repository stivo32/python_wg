# coding: utf-8

n = 3

result = 1
for i in range(2, n + 1):
    result *= (1 - 1.0 / (i ** 2))
print result
