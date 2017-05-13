input = int(raw_input())
n_sum = 0
n_sq_sum = 0
for i in range(input+1):
    n_sum += i
    n_sq_sum += i ** 2

print n_sum, n_sq_sum