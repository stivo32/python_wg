input = int(raw_input())
n_sum = 0
n_sq_sum = 0
for i in range(input):
    number = int(raw_input())
    n_sum += number
    n_sq_sum += number ** 2

print n_sum, n_sq_sum