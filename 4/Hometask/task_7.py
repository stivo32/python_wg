# coding: utf-8
import math

bound = 10
final_sum = 0
for k in range(1, bound + 1):
    inner_sum = 0
    for n in range(1, k + 1):
        inner_sum += math.sin(k * n)
    factorial = 1
    for j in range(1, k + 1):
        factorial *= j
    final_sum += inner_sum / factorial

print final_sum
