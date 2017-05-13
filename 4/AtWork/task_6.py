#user_input = raw_input('>').split()

numbers = [2, 4, 4, 0, 6, 6, 8, 10, 20]

numbers.sort()
print numbers
numbers[2:-2] = []
print numbers
numbers[2:2] = range(numbers[1] + 1, numbers[-2])
print numbers
numbers.reverse()
print numbers
